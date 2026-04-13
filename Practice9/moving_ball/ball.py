import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Balls")

clock = pygame.time.Clock()


radius = 25
step = 5   


border_thickness = 10
offset = 20


circles = [[WIDTH // 2, HEIGHT // 2]]

while True:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                circles.append([WIDTH // 2, HEIGHT // 2])

   
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

  

    screen.fill((255, 255, 255))
    pygame.draw.rect(
        screen,
        (0, 0, 0),
        (0, offset, WIDTH, HEIGHT - offset),
        border_thickness
    )
    
    
    pygame.draw.circle(screen, (255, 0, 0), (circles[-1]), radius)
    
    pygame.display.flip()
    clock.tick(60)