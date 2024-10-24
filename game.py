import pygame
from helpers import build_background

WIDTH = 1260
HEIGHT = 720

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#make background
background = build_background(WIDTH, HEIGHT)


#start game
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #blit background to screen
    screen.blit(background,(0,0))

    # fill the screen with a color to wipe away anything from last frame
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()