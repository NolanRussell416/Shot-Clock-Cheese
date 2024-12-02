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
    Left_Goal = pygame.image.load('kenney_sports-pack/PNG/Elements/element (41).png')
    Left_Goal_corner1 = pygame.image.load('kenney_sports-pack/PNG/Elements/element (32).png') 
    Left_Goal_corner2 = pygame.image.load('kenney_sports-pack/PNG/Elements/element (50).png')
    Right_Goal = pygame.image.load('kenney_sports-pack/PNG/Elements/element (45).png')
    Right_Goal_corner1 = pygame.image.load('kenney_sports-pack/PNG/Elements/element (36).png') 
    Right_Goal_corner2 = pygame.image.load('kenney_sports-pack/PNG/Elements/element (54).png')
    TILE_SIZE = vertical.get_height()
    Goal_Size = Left_Goal.get_height()
    print(Goal_Size)
    
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
    for y in range(200,400,Goal_Size):
        background.blit(Left_Goal,(0,y))
    background.blit(Left_Goal_corner1, (0, 136))   
    background.blit(Left_Goal_corner2, (0, 456))
    for y in range(200,400,Goal_Size):
        background.blit(Right_Goal,(1195,y))
    background.blit(Right_Goal_corner1, (1195, 136))   
    background.blit(Right_Goal_corner2, (1195, 456))    
    return background

def make_instructions(screen, color):
    # black screen
    screen.fill(color)

    WIDTH = screen.get_width()

    instructions = [
        'Player 1 use the arrow keys to move your player',
        'Player 2 use WASD keys to move your player',
        'Press Spacebar to kick the ball',
        'Shoot into the goal to score',
        '',
        '**Press any Key To Play**'
    ]

    # make an instruction font
    i_font = pygame.font.Font('kenney_sports-pack/PNG/chunkfive/Chunkfive-Regular.otf', size=50)
    spacing = 80
    # render (make surface) for each instruction
    for ii in range(len(instructions)):
        # render the font
        font_surf = i_font.render(instructions[ii], True, (0,0,255))
        # get a rect
        font_rect = font_surf.get_rect()
        font_rect.center = (WIDTH//2, spacing + ii * spacing)
        # blit it to the screen
        screen.blit(font_surf, font_rect)


def loop_instructions(screen):
    waiting = 1
    running = True
    # if we see the spacebar, exit the loop (break)
    while waiting:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                waiting = 0
            if event.type == pygame.KEYDOWN:
                # if any key pressed, break
                waiting = 0
        
        make_instructions(screen, (0, 0, 0))

        pygame.display.flip()
    
    return running