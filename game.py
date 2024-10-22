import pygame

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True

#make a background
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH,HEIGHT))
light_green = (47,153,67)
dark_green = (47,173,67)
background.fill(dark_green)
stripe_width = 30
stripe = pygame.Surface((stripe_width, HEIGHT))
stripe.fill(light_green)
for x in range(0,WIDTH,stripe_width*2):
    background.blit(stripe,(x,0))

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