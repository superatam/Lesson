import pygame

from pygame import *
pygame.init()
screen = pygame.display.set_mode((600, 360))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    pygame.draw.ellipse(screen, (255, 0, 0), [300, 10, 50, 20])
    pygame.draw.circle(screen, (154, 0, 0), (250, 250), 75)
    pygame.display.flip()
pygame.quit() 