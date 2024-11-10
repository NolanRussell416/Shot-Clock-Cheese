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
    horizontal = pygame.image.load('kenney_sports-pack/PNG/Elements/element (2).png')
    corner1 = pygame.image.load('kenney_sports-pack/PNG/Elements/element (5).png')
    vertical = pygame.image.load('kenney_sports-pack/PNG/Elements/element (1).png')
    corner2 = pygame.image.load('kenney_sports-pack/PNG/Elements/element (23).png')
    corner3 = pygame.image.load('kenney_sports-pack/PNG/Elements/element (27).png')
    corner4 = pygame.image.load('kenney_sports-pack/PNG/Elements/element (9).png')
    TILE_SIZE = vertical.get_height()
    
    # loop over x direction
    for x in range(90,1140,TILE_SIZE):
            # blit the tile to our BG
            background.blit(horizontal,(x,10))
    background.blit(corner1, (30,10))
    for y in range(60,592,TILE_SIZE):
            # blit the tile to our BG
            background.blit(vertical, (30,y))
    background.blit(corner2, (30,610))
    for x in range(90,1140,TILE_SIZE):
            # blit the tile to our BG
            background.blit(horizontal, (x,610))
    background.blit(corner3, (1160,610))    
    for y in range(60,592,TILE_SIZE):
            # blit the tile to our BG
            background.blit(vertical, (1160,y))
    background.blit(corner4, (1160,10))        
    return background