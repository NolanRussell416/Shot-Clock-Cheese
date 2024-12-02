from math import cos, sin, pi
import pygame

WIDTH = 1260
HEIGHT = 720
class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, theta=270, color = 'green'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 0
        self.theta = theta # degrees
        self.color = color
        self.orig_image = pygame.image.load('kenney_sports-pack/PNG/Green/CharacterGreen (4).png')
        # else:
        #     self.orig_image = pygame.image.load('assets/Ships/ship (2).png')
        self.image = self.orig_image # keep orig image to never be rotated
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.image = self.orig_image # keep orig image to never be rotated
        self.rect = self.image.get_rect()
        self.max_speed = 5
        self.screen = screen
        self.reverse_time = pygame.time.get_ticks()
        self.length = self.rect.height + 5
        self.screen_w = WIDTH
        self.screen_h = HEIGHT
    
    def deg_to_rad(self, deg):
        # converts deg to rad
        rad = (deg/180) * pi
        return rad
    
    def check_keys(self):
        # check keys to move ship around
        keys = pygame.key.get_pressed()
        # check w,s up/down
        if keys[pygame.K_UP]:
            self.speed += 0.5
        if keys[pygame.K_DOWN]:
            self.speed -= 0.5
        # check a, d theta left/right
        if keys[pygame.K_LEFT]:
            self.theta += 2
        if keys[pygame.K_RIGHT]:
            self.theta -= 2
    
    def check_border(self):
        # make sure our player rect is inside of some rect we set
        border_rect = pygame.rect.Rect(0, 0, self.screen_w, self.screen_h)
        #if the ships rectangle leaves border, then set speed to 0
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

    def update(self):
        self.check_keys() # only red if influenced by keys
        
        # check and make sure we are moving too fast
        if self.speed > self.max_speed:
            self.speed = self.max_speed 
        elif self.speed < -self.max_speed:
            self.speed = -self.max_speed
          
        # get x and y components of speed
        theta_rad = self.deg_to_rad(self.theta)
        x_dot = cos(theta_rad) * self.speed
        y_dot = sin(theta_rad) * self.speed

        self.x += x_dot
        self.y -= y_dot

        # now rotate the image and drew new rect
        self.image = pygame.transform.rotozoom(self.orig_image, self.theta, 0.7)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.check_border()