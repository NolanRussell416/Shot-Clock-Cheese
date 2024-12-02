import pygame
from helpers import build_background
from game_character import Player
WIDTH = 1260
HEIGHT = 720

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#make background
background = build_background(WIDTH, HEIGHT)

#make character
player1 = Player(screen,200,200, WIDTH, HEIGHT)
team_group = pygame.sprite.Group()

# add our sprite to the sprite group
team_group.add(player1) 

#start game
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    team_group.update()

    #blit background to screen
    screen.blit(background,(0,0))

    #draw player
    team_group.draw(screen)

    # fill the screen with a color to wipe away anything from last frame
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()