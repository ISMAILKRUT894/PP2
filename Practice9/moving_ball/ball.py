import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Balls")

clock = pygame.time.Clock()

# Circle settings
radius = 25
step = 5   # меньше шаг = плавнее движение

# Border settings
border_thickness = 10
offset = 20

# List of circles
circles = [[WIDTH // 2, HEIGHT // 2]]

while True:
    # --- EVENTS ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ➕ Создание нового круга (один раз при нажатии)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                circles.append([WIDTH // 2, HEIGHT // 2])

    # --- MOVEMENT (при удержании) ---
    keys = pygame.key.get_pressed()

    x, y = circles[-1]

    if keys[pygame.K_UP]:
        if y - step - radius >= border_thickness + offset:
            y -= step

    if keys[pygame.K_DOWN]:
        if y + step + radius <= HEIGHT - border_thickness:
            y += step

    if keys[pygame.K_LEFT]:
        if x - step - radius >= border_thickness:
            x -= step

    if keys[pygame.K_RIGHT]:
        if x + step + radius <= WIDTH - border_thickness:
            x += step

    circles[-1] = [x, y]

    # --- DRAW ---
    screen.fill((255, 255, 255))

    pygame.draw.rect(
        screen,
        (0, 0, 0),
        (0, offset, WIDTH, HEIGHT - offset),
        border_thickness
    )

    for (cx, cy) in circles:
        pygame.draw.circle(screen, (255, 0, 0), (cx, cy), radius)

    pygame.display.flip()
    clock.tick(60)