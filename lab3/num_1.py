import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
circle(screen, (255, 255, 0), (200, 150), 150)
line(screen, (0, 0, 0), (120, 230), (280,230),30)


circle(screen, (255, 0, 0), (130, 100), 25)
circle(screen, (0, 0, 0), (130, 100), 25,1)
circle(screen, (0, 0, 0), (130, 100), 12)

circle(screen, (255, 0, 0), (270, 100), 17)
circle(screen, (0, 0, 0), (270, 100), 17,1)
circle(screen, (0, 0, 0), (270, 100), 8)

line(screen, (0,0,0), (50,10),(170,90),15)
line(screen, (0,0,0), (370,30),(220,90),15)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
