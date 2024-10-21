#import pygame and initialize the pygame engine.
import pygame
import random
import time
from pygame.locals import *
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((640,480))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
#The Game Loop”
color=(0,255,0)
w=0
h=0
drag=False
while True:
    screen.fill((0,0,0))
    if w!=0 and h!=0:
        pygame.draw.rect(screen,(255,100,0), (x,y, w, h), 0)
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            screen.fill((0,0,0))
            x,y=event.pos
            
            drag = True
            
        if drag == True:
            if event.type == MOUSEBUTTONUP:
                drag=False
                x2,y2=event.pos
                w=x2-x
                h=y2-y

        if drag == True:
            if event.type == MOUSEMOTION:
                x2,y2=event.pos
                w=x2-x
                h=y2-y 
                
                
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
