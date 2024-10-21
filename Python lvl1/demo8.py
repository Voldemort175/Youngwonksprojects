import pygame
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!")
x=300
y=300
up=False
down=False
left=False
right=False
while True:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255),(x,y),50)
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_RIGHT:
                right=True
                left=False
                up=False
                down=False
            if event.key==K_LEFT:
                left=True
                right=False
                up=False
                down=False
            if event.key==K_UP:
                up=True
                right=False
                left=False
                down=False
            if event.key==K_DOWN:
                down=True
                right=False
                left=False
                up=False
        elif event.type==KEYUP:
            if event.key==K_RIGHT:
                right=False
            if event.key==K_LEFT:
                left=False
            if event.key==K_UP:
                up=False
            if event.key==K_DOWN:
                down=False
    if right==True:
        x=x+5
    if left==True:
        x=x-5
    if up==True:
        y=y-5
    if down==True:
        y=y+5
       
    pygame.display.update()
