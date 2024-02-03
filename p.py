import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Kolory
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paletka
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (50, HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

# Grupa sprite'ów dla paletki
all_sprites = pygame.sprite.Group()
paddle = Paddle()
all_sprites.add(paddle)

# Pętla gry
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Aktualizacja paletki
    all_sprites.update()

    # Rysowanie tła
    screen.fill(BLACK)

    # Rysowanie paletki
    all_sprites.draw(screen)

    # Aktualizacja okna
    pygame.display.flip()

    # Ustawienie liczby klatek na sekundę
    clock.tick(60)