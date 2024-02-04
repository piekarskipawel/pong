import sys
import pygame
from settings import Settings
from paddle import PaddleOne, PaddleTwo
from ball import Ball
import random

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

        self.game_active = False  # Dodane, aby kontrolować, czy gra jest aktywna

        self.player1_score = 0
        self.player2_score = 0

    # Funkcja do wyświetlania tekstu startowego na ekranie
    def display_text(self):
        self.font_display_text = pygame.font.Font(None, 36)
        self.start_text = self.font_display_text.render("PRESS SPACE TO START GAME", True, self.settings.score_color)
        self.screen.blit(self.start_text, (self.settings.screen_width // 2 - 190, self.settings.screen_height // 2))
            
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game_active = True
                    self.ball.active = True  # Dodane, aby aktywować ruch piłki
                    self.ball.speed = [random.choice([-5, 5]), random.choice([-5, 5])]
            
            if self.game_active:  
                self.all_sprites.update()                
                           
                # Odbicie od ścian
                if self.ball.rect.top <= 0 or self.ball.rect.bottom >= self.settings.screen_height:
                    self.ball.speed[1] = -self.ball.speed[1]    
            
                # Sprawdzenie kolizji piłki z paletkami
                if pygame.sprite.spritecollide(self.paddle_one, [self.ball], False) or pygame.sprite.spritecollide(self.paddle_two, [self.ball], False):
                    self.ball.speed[0] = -self.ball.speed[0]
            
                # Redraw the screen during each pass through the loop.
                self.screen.fill(self.settings.bg_color)
                self.all_sprites.draw(self.screen)
            

                # Wyświetlanie wyniku
                font = pygame.font.Font(None, 36)
                player1_text = font.render(f"Player 1: {self.player1_score}", True, self.settings.score_color)
                player2_text = font.render(f"Player 2: {self.player2_score}", True, self.settings.score_color)
                self.screen.blit(player1_text, (50, 50))
                self.screen.blit(player2_text, (self.settings.screen_width - 200, 50))

                # Resetowanie piłki i zliczanie punktu, jeśli wyleci za boisko
                if self.ball.rect.left <= 0:
                    self.ball.reset_ball()
                    self.player2_score += 1  # Zwiększanie punktu dla drugiego gracza
                    

                if self.ball.rect.right >= self.settings.screen_width:
                    self.ball.reset_ball()
                    self.player1_score += 1  # Zwiększanie punktu dla pierwszego gracza
            else:
                self.display_text()


            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pong = Pong()
    pong.run_game()    