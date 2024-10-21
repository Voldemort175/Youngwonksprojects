#Question 2
import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!")
cord=300
cord2=[random.randint(30,570),30]
flag = False
dire = ""
while True:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(225,225,225),(cord,500,100,20))
    pygame.draw.circle(screen,[225,0,0],(cord2[0],cord2[1]),30,3)
    cord2[1]=cord2[1]+50
    while True:
        cord2[0]=random.randint(cord2[0]-100,cord2[0]+100)
        if 30<cord2[0]<570:
            break
    time.sleep(0.5)
    if cord2[1]>600:
        cord2=[random.randint(30,570),30]
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key==K_RIGHT:
                flag = True
                dire = "right"
            if event.key==K_LEFT:
                flag = True
                dire = "left"
    if dire == "right":
        cord=cord+50
    if dire == "left":
        cord=cord-50
    if cord>600:
        cord=0
    elif cord<0:
        cord=600
    pygame.display.update()
