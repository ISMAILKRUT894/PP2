import pygame
pygame.init()
screen = pygame.display.set_mode((800,300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 53, 255))  # clear screen
    
    pygame.display.update()