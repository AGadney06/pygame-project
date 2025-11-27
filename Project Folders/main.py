import pygame, sys #imports pygame
from player import Player #Imports the Player class from player.py to main.py
import obstacle

class Game:
    def __init__(self): #Constructor
        # Player setup
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
    
    def run(self):
        self.player.sprite.lasers.draw(screen) #Draws the lasers to the screen
        self.player.update()
        self.player.draw(screen)
        self.blocks.draw(screen)

pygame.init()
screen_width = 600 #Sets the window's width
screen_height = 600 #Sets the window's height
screen = pygame.display.set_mode((screen_width,screen_height)) #Uses screen_width & screen_height to create a display
clock = pygame.time.Clock() #Game clock
game = Game()

while True:
    for event in pygame.event.get(): #Checks for the escape key to exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((30,30,30)) #Draws the background colour
    game.run() #Calls back to the run function

    pygame.display.flip()
    clock.tick(60) # Uses the previously mentioned clock to set the game's fps