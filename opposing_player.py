from game_character import Player
from math import atan2, degrees, radians, cos, sin, pi
import pygame

class Opposing_Player(Player):
    def __init__(self, screen, x, y, theta=180, color = 'red'):
        super().__init__(screen, x, y, theta, color)
        self.color = color 

    def deg_to_rad(self, deg):
        # converts deg to rad
        rad = (deg/180) * pi
        return rad
    
    def enemy_check_keys(self):
        # check keys to move player around
        keys = pygame.key.get_pressed()

        # check up, down keys 
        if keys[pygame.K_UP]:
            self.speed += 0.2
        if keys[pygame.K_DOWN]:
            self.speed -= 0.2
        # check left, right keys
        if keys[pygame.K_LEFT]:
            self.theta += 3
        if keys[pygame.K_RIGHT]:
            self.theta -= 3

    def check_border(self):
        # make sure our player rect is inside of some rect we set
        border_rect = pygame.rect.Rect(0, 0, self.screen_w, self.screen_h)
        #if the player rectangle leaves border, then set speed to 0
        if not border_rect.contains(self.rect):
            # only reverse if its been >500ms from last time
            if pygame.time.get_ticks() - self.reverse_time > 500:
                self.speed = -0.2 * self.speed
                # reset the timer
                self.reverse_time = pygame.time.get_ticks()
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_w:
            self.rect.right = self.screen_w
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_h:
            self.rect.bottom = self.screen_h
    
    def check_collision(self, player):
        # Check if the player's rect collides with another object's rect
        return self.rect.colliderect(player)

    def update(self):
        if self.color == 'green':   
            self.check_keys() #wasd keys
        else:
            self.enemy_check_keys()#arrow keys
          
        # get x and y components of speed
        theta_rad = self.deg_to_rad(self.theta)
        dx = cos(theta_rad) * self.speed
        dy = sin(theta_rad) * self.speed

        self.x += dx
        self.y -= dy

        # check and make sure we are moving too fast
        if self.speed > self.max_speed:
            self.speed = self.max_speed 
        elif self.speed < -self.max_speed:
            self.speed = -self.max_speed
        
        # now rotate the image and draw new rect
        self.image = pygame.transform.rotozoom(self.orig_image, self.theta, 2)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.check_border()