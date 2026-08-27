import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sort Visualizer")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (120, 150, 255), (300, 200, 80, 80))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()