import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 30)

# Snake
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# Generate food position
def generate_food_position():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)

# Food class
class Food:
    def __init__(self):
        self.position = generate_food_position()
        self.weight = random.choice([1, 2, 3])
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = random.randint(3000, 7000)  

    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > self.lifetime

    def get_color(self):
        if self.weight == 1:
            return RED
        elif self.weight == 2:
            return ORANGE
        else:
            return YELLOW

# Create first food
food = Food()

# Game variables
score = 0
level = 1
speed = 7

running = True
while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)

    # Move snake
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Wall collision
    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT
    ):
        print("Game Over: Hit the wall")
        running = False

    # Self collision
    if head in snake:
        print("Game Over: Hit yourself")
        running = False

    snake.insert(0, head)

    # Food expiration
    if food.is_expired():
        food = Food()

    # Food collision
    if head == food.position:
        score += food.weight
        food = Food()

        # Level system
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, food.get_color(), (*food.position, CELL_SIZE, CELL_SIZE))

    # UI text
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()