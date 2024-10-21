#import pygame and initialize the pygame engine.
import pygame
import random
import time
import math
from pygame.locals import *
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((600,600))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
#The Game Loop”
color=(0,255,0)
r=10
cnt=0
drag=False
while True:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,color, (300,300),r,0)
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            #print(event)
            cnt+=1
            x,y=event.pos
            sqx=(x-300)**2
            sqy=(y-300)**2
            if event.button == 3:
                if math.sqrt(sqx + sqy)<r:
                    r/=2
            if cnt%2==0:
                if math.sqrt(sqx + sqy)<r:
                    r*=2
            
        if event.type == MOUSEBUTTONUP:
            drag=False

        if drag == True:
            if event.type == MOUSEMOTION:
                x_circ, y_circ = event.pos
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
