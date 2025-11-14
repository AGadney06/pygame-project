import pygame
import sys

pygame.init()

class Player:
    def __init__(self, x, y, img, l, h):
        self.x = x
        self.y = y
        self.img = img
        self.l = l
        self.h = h
        self.img = pygame.transform.scale(img, (l, h))
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)

class Invader:
    def __init__(self, x, y, alien_type, l, h):
        self.x = x
        self.y = y
        self.alien_type = alien_type
        self.l = l
        self.h = h

        if self.alien_type == 1:
            self.img_path = "Project/invader1.png" # Bottom row
            self.score = 10
        elif self.alien_type == 2:
            self.img_path = "Project/invader2.png" # Middle rows
            self.score = 20
        else:
            self.img_path = "Project/invader3.png" # Top row
            self.score = 30

        self.img = pygame.image.load(self.img_path)
        self.img = pygame.transform.scale(self.img, (l, h))
        self.rect = pygame.Rect(self.x, self.y, self.l, self.h)

class Bullet:
    def __init__(self, x, y, w, h, s):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.speed = s
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

screen = pygame.display.set_mode([SCREEN_HEIGHT,SCREEN_WIDTH])

clock = pygame.time.Clock() # to slow down the speed of movement
FPS = 15 # to slow down the speed of movement

player = Player((SCREEN_WIDTH/2)-(35/2), (SCREEN_HEIGHT - 100), pygame.image.load("Project/defender.png"), 35, 35)

invader = Invader(250, 100, 1, 30, 30) 
invaders = [] # ready for an array of invaders
invaders.append(invader)

moveRight = True
fired = False

bullet = Bullet(player.x, player.y, 10, 20, 10)
bullets = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= 5
            elif event.key == pygame.K_RIGHT:
                player.x += 5
            elif event.key == pygame.K_SPACE:
                # --- FIX 6: Only fire if a bullet isn't already 'fired' ---
                if not fired:
                    fired = True
                    bullet.x = player.x + (player.l / 2) - (bullet.width / 2) # Center bullet
                    bullet.y = player.y
            elif event.key == pygame.K_ESCAPE: # TO QUIT
                running = False

    screen.fill([0,0,0]) # black background
    screen.blit(player.img, (player.x, player.y))

    for inv in invaders:
        screen.blit(inv.img, (inv.x, inv.y))

    if player.x < 0:
        player.x = 0
    if player.x > SCREEN_WIDTH - player.l:
        player.x = SCREEN_WIDTH - player.l
    
    player.rect.x = player.x

    if fired == True:
        pygame.draw.rect(screen, [0,255,0], bullet.rect)
        bullet.y -= bullet.speed
        bullet.update() # Update the bullet's rect position
        
        if bullet.y < 0:
            fired = False
            

        for inv in invaders: # Check against each invader
            if bullet.rect.colliderect(inv.rect):
                invaders.remove(inv) # Remove the invader that was hit
                fired = False        # Allow a new bullet to be fired
                bullet.x = -100      # Move bullet off-screen
                bullet.y = -100
                break # Stop checking collisions for this bullet

    pygame.display.flip()

    clock.tick(FPS)

# Quit Pygame and exit the program
pygame.display.quit()
pygame.quit()
sys.exit(0)