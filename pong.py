import sys
import pygame
from settings import Settings
from paddle import PaddleOne, PaddleTwo
from ball import Ball

class Pong():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Pong")
        
        # Grupa sprite'ów dla paletki
        self.paddle_one = PaddleOne()
        self.paddle_two = PaddleTwo()
        self.ball = Ball()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.paddle_one,self.paddle_two, self.ball)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            
            # Sprawdzenie kolizji piłki z paletkami
            if pygame.sprite.spritecollide(self.paddle_one, [self.ball], False) or pygame.sprite.spritecollide(self.paddle_two, [self.ball], False):
                self.ball.speed[0] = -self.ball.speed[0]
            
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pong = Pong()
    pong.run_game()