import pygame #imports pygame
import sys
from player import Player #Imports the Player class from player.py to main.py

class Game:
    def __init__(self): #Constructor
        player_sprite = Player((screen_width/2,screen_height),screen_width,5)#The player sprite and its starting position at the bottom middle of the screen
        self.player = pygame.sprite.GroupSingle(player_sprite) #Group single with player sprite inside of it

    def run(self):
        self.player.sprite.lasers.draw(screen) #Draws the lasers to the screen
        self.player.update()
        self.player.draw(screen)

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