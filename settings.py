import random

class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.score_color = (255,255,255)
        self.start_game_color = (255,255,255)

        # paddle settings
        self.paddle_color = (255,255,255)
        self.speed_paddle_one = 7
        self.speed_paddle_two = 7

        # ball settings
        self.ball_color = (255,255,255)
        self.ball_speed = [random.choice([-7, 7]), random.choice([-7, 7])]


        
        
