import pygame
from pygame.draw import *

pygame.init()
def popugai(x, y, n):
    polygon(screen, (0, 0, 0), [[x, y], [x+4*n, y-n], [x+10*n, y+3*n], [x+12*n, y+n], [x+18*n, y], [x+10*n, y+6*n]])

FPS = 30
screen = pygame.display.set_mode((900, 700))
screen.fill((244, 164, 96))

line(screen,(255,218,185),(0,300),(1500,250),150)
polygon(screen,(255,165,0),[(0,360),(20,290),(200,210),(240,230),(260,260),(360,330),(410,330),(450,360),(490,300),(530,320),(550,300),(550,280),(650,170),(770,280),(900,250),(900,355)])

circle(screen,(255,255,0),(450,200),70)
ellipse(screen,(178,34,34),(-10,400,100,150))
ellipse(screen,(178,34,34),(50,370,120,200))

polygon(screen,(178,34,34),[(130,500),(200,390),(300,450),(320,370),(420,380),(490,440),(590,420),(590,1000)])
ellipse(screen,(178,34,34),(580,350,100,200))
polygon(screen,(178,34,34),[(670,400),(690,460),(695,480),(670,480)])
polygon(screen,(178,34,34),[(650,480),(740,400),(780,470),(810,430),(850,440),(950,300),(950,1000)])



line(screen,(216,191,216),(0,600),(1500,600),250)


popugai(100, 100, 2)
popugai(140, 110, 2)
popugai(110, 160, 3)
popugai(150, 170, 4)
popugai(400, 350, 3)

polygon(screen, (55, 0, 100), [
    [0, 600], [0, 420], [200, 440], [400, 540], [500, 590], [600, 550],
    [680, 570], [900, 430], [900, 600]
    ])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
