from math import cos, sin, radians
import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, theta, speed = 0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed
        self.theta = theta # degrees
        self.image = pygame.image.load('kenney_sports-pack/PNG/Equipment/ball_soccer2.png')
        self.rect = self.image.get_rect()
        # place the ball
        self.rect.center=(self.x, self.y)
        self.screen = screen

    def check_collision(self, player):
        # Check if the player's rect collides with another object's rect
        return self.rect.colliderect(player)
    def check_keys(self):
        # check keys to move ship around
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.speed += 10
    
    def reset(self):
        if self.x>1195:
            self.x = 1260//2
            self.y = 720//2
        if self.x<30:
            self.x = 1260//2
            self.y = 720//2
        if self.y>660:
            self.x = 1260//2
            self.y = 720//2
        if self.y<35:
            self.x = 1260//2
            self.y = 720//2
        
    def update(self):
        dx = self.speed * cos(radians(self.theta))
        dy = self.speed * sin(radians(self.theta))
        self.x += dx
        self.y -= dy
        self.speed=0.95*self.speed 
        self.reset()
        # update the rect
        self.rect.center = (self.x,self.y)