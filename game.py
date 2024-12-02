import pygame
from helpers import build_background, loop_instructions
from game_character import Player
from ball import Ball
from opposing_player import Opposing_Player

WIDTH = 1260
HEIGHT = 720

# pygame setup
pygame.init()
pygame.mixer.init()

bg_music = pygame.mixer.Sound('kenney_sports-pack/PNG/spotifydown.com - Dança do Pombo.mp3')
bg_music.play(-1)
clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#make background
background = build_background(WIDTH, HEIGHT)

keys = pygame.key.get_pressed()
#make character
team_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

#make ball
ball1 = Ball(screen, WIDTH//2, HEIGHT//2, 0)

#make players
player1 = Player(screen, 200, 360)
enemy1 = Opposing_Player(screen, 900, 360)

# add our sprite to the sprite group
team_group.add(player1) 
enemy_group.add(enemy1)

P1score = [0]
P2score =[0]
score_font = pygame.font.Font('kenney_sports-pack/PNG/quicksand/Quicksand-Bold.otf', size=40)

running = loop_instructions(screen)
#start game
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    team_group.update()
    enemy_group.update()

    #add ball collision
    if ball1.check_collision(player1):
        ball1.theta = player1.theta
        ball1.speed+=1
        ball1.check_keys()
    if ball1.check_collision(enemy1):
        ball1.theta = enemy1.theta
        ball1.speed+=1
        ball1.check_keys()

    #add player collision
    if player1.check_collision(enemy1):
        enemy1.speed = -0.7 * enemy1.speed
        player1.speed = -0.7 * player1.speed

    #blit background to screen
    screen.blit(background,(0,0))

    #draw players, ball, and score
    black = pygame.Color('#000000')
    score_text = f"Green: {P1score[0]} | Red: {P2score[0]}"
    score_surface = score_font.render(score_text, 1, black)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (0,0)
    screen.blit(score_surface, score_rect)
    ball1.update()
    screen.blit(ball1.image, ball1.rect)
    team_group.draw(screen)
    enemy_group.draw(screen)

    #add scoring
    if 1190 < ball1.x < WIDTH and 175 < ball1.y < 485:
        ball1.x = 1260//2
        ball1.y = 720//2
        P1score[0] += 1
    if 0 < ball1.x < 50 and 175 < ball1.y < 485:
        ball1.x = 1260//2
        ball1.y = 720//2
        P2score[0] += 1

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()