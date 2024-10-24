import pygame
def build_background(WIDTH, HEIGHT):
    #build base
    background = pygame.Surface((WIDTH,HEIGHT))
    light_green = (47,153,67)
    dark_green = (47,173,67)
    background.fill(dark_green)
    stripe_width = 30
    stripe = pygame.Surface((stripe_width, HEIGHT))
    stripe.fill(light_green)
    for x in range(0,WIDTH,stripe_width*2):
        background.blit(stripe,(x,0))

    #add layers
    horizontal = pygame.image.load('kenney_sports-pack/PNG/Elements/Element (2).png')
    TILE_SIZE = horizontal.get_width()

    # # loop over x direction
    # for x in range(0,WIDTH,TILE_SIZE):
    #     # loop over y direction
    #     for y in range(0,700, TILE_SIZE):
    #         # blit the tile to our BG
    #         background.blit(horizontal, (x,y))
        
    return background