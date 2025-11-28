import pygame #imports pygame
import sys
from player import Player #Imports the Player class from player.py to main.py
from alien import Alien
from random import choice
from laser import Laser
import obstacle

class Game:
    def __init__(self): #Constructor
        #Player Setup
        player_sprite = Player((screen_width/2,screen_height),screen_width,5)#The player sprite and its starting position at the bottom middle of the screen
        self.player = pygame.sprite.GroupSingle(player_sprite) #Group single with player sprite inside of it
        
        # obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions,x_start = screen_width / 15, y_start = 480)

    def create_obstacle(self, x_start, y_start,offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index,col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size,(201,17,14),x,y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self,*offset,x_start,y_start):
        for offset_x in offset:
            self.create_obstacle(x_start,y_start,offset_x)  


        #Alien Setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)
        self.alien_direction = 1
        self.alien_lasers = pygame.sprite.Group()

    def alien_setup(self,rows,cols,x_distance = 60 ,y_distance = 48,x_offset = 70, y_offset = 100):
        for row_index, row in enumerate(range(rows)): #Determines what row we are talking about
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                

                if row_index == 0:
                    alien_sprite = Alien('invader1',x,y) #On row 0, print out this alien type
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien('invader2',x,y) #On row 1 and row 2, print out this alien type
                else:
                    alien_sprite = Alien('invader3',x,y)
                self.aliens.add(alien_sprite) #On every other row, print out this alien type

    def alien_location_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width: 
                self.alien_direction = -1 #if the right direction of the aliens exceeds the width of the game window change their direction to -1
                self.alien_move_down(2) #Move aliens down by 2
            elif alien.rect.left <= 0:
                self.alien_direction = 1 #if the left direction of the aliens exceeds the width of the game window change their direction to 1
                self.alien_move_down(2) #Move aliens down by 2

    def alien_move_down(self,distance):
        if self.aliens: #If there are still aliens on screen
            for alien in self.aliens.sprites():
                alien.rect.y += distance
    
    def alien_shoot(self):
        if self.aliens.sprites(): #If aliens are still on screen
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center,6,screen_height)
            self.alien_lasers.add(laser_sprite)
    
    def collision_check(self):
        #Player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                #Obstacle collision
                if pygame.sprite.spritecollide(laser,self.blocks,True): #Obstacle Collision from player lasers
                    laser.kill()
                
                #Alien colissions
                if pygame.sprite.spritecollide(laser,self.aliens,True):
                    laser.kill()
                
        #Alien lasers
        if self.alien_lasers:
            for laser in self.alien_lasers:
                if pygame.sprite.spritecollide(laser,self.blocks,True): #Obstacle Collission from alien lasers
                    laser.kill()
                #Player colissions
                if pygame.sprite.spritecollide(laser,self.player,False):
                    laser.kill()
                    print('U R DEAD')
        
        if self.aliens:
            for alien in self.aliens:
                #pygame.sprite.spritecollide(alien,self.blocks,True)

                if pygame.sprite.spritecollide(alien,self.player,False):
                    pygame.quit()
                    sys.exit()
    
    def run(self):
        self.player.sprite.lasers.draw(screen) #Draws the lasers to the screen
        self.player.update()
        self.player.draw(screen) #Draws the player to the screen
        self.blocks.draw(screen)
        self.aliens.update(self.alien_direction)
        self.aliens.draw(screen) #Draws the Aliens to the screen
        self.alien_location_checker()
        self.alien_lasers.update()
        self.alien_lasers.draw(screen)
        self.collision_check()


if __name__ == '__main__':
    pygame.init() #Initialises pygame
    screen_width = 600 #Sets the window's width
    screen_height = 600 #Sets the window's height
    screen = pygame.display.set_mode((screen_width,screen_height)) #Uses screen_width & screen_height to create a display
    clock = pygame.time.Clock() #Game clock
    game = Game()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER,800) #Waits 800 milliseconds before activating the ALIENLASER event again

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #Checks for the escape key to exit the game
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER: #If the alien's laser event is called also call alien_shoot
                game.alien_shoot()
        
        screen.fill((0,0,0)) #Draws the background colour
        game.run() #Calls back to the run function

        pygame.display.flip()
        clock.tick(60) # Uses the previously mentioned clock to set the game's fps