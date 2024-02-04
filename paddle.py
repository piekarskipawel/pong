import pygame
from settings import Settings

class PaddleOne(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.settings = Settings()
        self.image = pygame.Surface((20, 100))
        self.image.fill(self.settings.paddle_color)
        self.rect = self.image.get_rect()
        self.rect.center = (50, self.settings.screen_height // 2)
        
    def update(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.settings.speed_paddle_one
        if keys[pygame.K_s] and self.rect.bottom < self.settings.screen_height:
            self.rect.y += self.settings.speed_paddle_one
    
    def reset_paddle_one(self):
        self.settings = Settings()
        self.image = pygame.Surface((20, 100))
        self.image.fill(self.settings.paddle_color)
        self.rect = self.image.get_rect()
        self.rect.center = (50, self.settings.screen_height // 2)

            
class PaddleTwo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.settings = Settings()
        self.image = pygame.Surface((20, 100))
        self.image.fill(self.settings.paddle_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.settings.screen_width - 50, self.settings.screen_height // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.settings.speed_paddle_two
        if keys[pygame.K_DOWN] and self.rect.bottom < self.settings.screen_height:
            self.rect.y += self.settings.speed_paddle_two

    def reset_paddle_two(self):
        self.settings = Settings()
        self.image = pygame.Surface((20, 100))
        self.image.fill(self.settings.paddle_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.settings.screen_width - 50, self.settings.screen_height // 2)