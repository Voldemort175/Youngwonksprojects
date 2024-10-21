import pygame
import time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Moving Circle")
blue=(0,0,255)
black=(0,0,0)
bally=250
ballx=250
Right=False
Left=False
Up=False
Down=False
rkey=False
lkey=False
ukey=False
dkey=False
while True:
    screen.fill(black)
    pygame.draw.circle(screen,blue,(ballx,bally),30,40)
    if Right == True:
        ballx=ballx+4
        if ballx >= 515:
            ballx=-15
    if Left == True:
        ballx=ballx-4
        if ballx <= -15:
            ballx=515
    if Up == True:
        bally=bally-4
        if bally <= -15:
            bally=515
    if Down == True:
        bally=bally+4
        if bally >= 515:
            bally=-15
    time.sleep(0.4)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key==K_RIGHT and lkey==False:
                Right=True
                Left=False
                Up=False
                Down=False
                rkey=True
                ukey=False
                dkey=False
            elif event.key==K_LEFT and rkey==False:
                Right=False
                Left=True
                Up=False
                Down=False
                lkey=True
                ukey=False
                dkey=False
            elif event.key==K_UP and dkey==False:
                Right=False
                Left=False
                Up=True
                Down=False
                ukey=True
                rkey=False
                lkey=False
            elif event.key==K_DOWN and ukey==False:
                Right=False
                Left=False
                Up=False
                Down=True
                dkey=True
                rkey=False
                lkey=False
    pygame.display.update()
