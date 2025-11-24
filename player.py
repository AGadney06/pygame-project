import pygame #imports pygame
from laser import Laser

class Player(pygame.sprite.Sprite): #Player class for the player sprite
    def __init__(self,pos,restriction,speed): #Constructor
        super().__init__() #Calls the constructor to inherit its attributes
        self.image = pygame.image.load('defender.png') #loads the defender.png file
        self.image = pygame.transform.scale(self.image, (50,50)) #Resizes the player sprite to a more appropriate size
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed #Speed of player
        self.max_x_restriction = restriction #The x coordinate boundaries of the game
        self.ready = True
        self.laster_time = 0
        self.laser_cooldown = 600

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]: #If the right key is pressed move the player to the right
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]: #If the left key is pressed move the player to the left
            self.rect.x -= self.speed
    
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks() #Checks the timer once

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks() #Checks the timer continuously until the cooldown reaches its maximum 
            if current_time - self.laser_time >= self.laser_cooldown: #Checks to see if the timer has reached the end of the cooldown period
                self.ready = True #The laser is now ready again to fire
    def restriction(self):
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= self.max_x_restriction:
            self.rect.right = self.max_x_restriction

    def shoot_laser(self): #shoot laser function
        print('shoot laser')

    def update(self):
        self.get_input()
        self.restriction()
        self.recharge()
    
