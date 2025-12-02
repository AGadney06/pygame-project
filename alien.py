import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self,type,x,y,speed):
        super().__init__() #Calls the constructor to inherit its attributes
        file_path = '../Project/' +  type + '.png'
        self.image = pygame.image.load(file_path).convert_alpha() #Loads alien image
        self.image = pygame.transform.scale(self.image, (50,50)) #Rescales alien image
        self.rect = self.image.get_rect(topleft = (x,y)) #Sets the rectangle for the alien
        self.speed = speed #Alien Speed


    def update(self,direction,alien_speed):
        self.speed = alien_speed
        self.rect.x += direction * self.speed #Alien direction x alien speed

        