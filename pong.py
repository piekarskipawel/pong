'''
Pong Game, author: Pawel Piekarski, e-mail: pawpiek@gmail.com
'''

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
        
        # Group of sprites for paddles and ball
        self.paddle_one = PaddleOne()
        self.paddle_two = PaddleTwo()
        self.ball = Ball()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.paddle_one,self.paddle_two, self.ball)

        self.game_active = False  # controlling if the game is active

        self.player1_score = 0
        self.player2_score = 0
    
    def display_text(self):
        '''Start message'''
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
                    self.ball.active = True  # controlling move of ball
                    self.ball.speed = self.settings.ball_speed
            
            if self.game_active:  
                self.all_sprites.update()

                # Bouncing the ball off the walls
                if self.ball.rect.top <= 0 or self.ball.rect.bottom >= self.settings.screen_height:
                    self.ball.speed[1] = -self.ball.speed[1]    
            
                # Checking the collision of the ball with the paddles
                if pygame.sprite.spritecollide(self.paddle_one, [self.ball], False) or pygame.sprite.spritecollide(self.paddle_two, [self.ball], False):
                    self.ball.speed[0] = -self.ball.speed[0]
            
                # Redraw the screen during each pass through the loop.
                self.screen.fill(self.settings.bg_color)
                self.all_sprites.draw(self.screen)
            
                # Display score
                font = pygame.font.Font(None, 56)
                player1_text = font.render(f"{self.player1_score}", True, self.settings.score_color)
                player2_text = font.render(f"{self.player2_score}", True, self.settings.score_color)
                self.screen.blit(player1_text, (200, 50))
                self.screen.blit(player2_text, (self.settings.screen_width - 200, 50))

                # Resetting the ball and counting the point if behind the field
                if self.ball.rect.left <= 0:
                    self.paddle_one.reset_paddle_one()
                    self.paddle_two.reset_paddle_two()
                    self.ball.reset_ball()
                    self.player2_score += 1  # Increasing the point for the first player
                    
                if self.ball.rect.right >= self.settings.screen_width:
                    self.paddle_one.reset_paddle_one()
                    self.paddle_two.reset_paddle_two()
                    self.ball.reset_ball()
                    self.player1_score += 1   #Increasing the point for the second player
                                    
            else:
                self.display_text()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pong = Pong()
    pong.run_game()    