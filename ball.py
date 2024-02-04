import pygame
from settings import Settings
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.settings = Settings()
        self.image = pygame.Surface((20, 20))
        self.image.fill(self.settings.ball_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)
        self.speed = [random.choice([-5, 5]), random.choice([-5, 5])]
        self.active = False  # Dodane, aby kontrolować aktywność piłki

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def reset_ball(self):
        self.active = False
        self.rect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)
        self.speed = [0, 0]
        

    

           
        
  