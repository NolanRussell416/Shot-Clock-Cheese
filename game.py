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
player1 = Player(200,200)

#start game
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #move character
    if event.type == pygame.KEYDOWN:
            k = pygame.key.name(event.key)
            # check if k is right, left, up down
            if k == 'right':
                player1.theta -= 1
            elif k == 'left':
                player1.theta += 1
            elif k == 'up':
                player1.speed += 0.1
            elif k == 'down':
                player1.speed -= 0.1

    # update the ships position
    player1.update()

    #blit background to screen
    screen.blit(background,(0,0))

    #draw player
    player1.draw(screen)

    # fill the screen with a color to wipe away anything from last frame
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()