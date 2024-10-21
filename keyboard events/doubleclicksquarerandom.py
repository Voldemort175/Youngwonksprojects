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
while True:
    pygame.draw.rect(screen,(255,100,0), (0,0, 20, 20), 0)
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            #print(event)
            cnt+=1
            x,y=event.pos
            if x<=20 and y<=20:
                if cnt%2==0:
                   pygame.draw.rect(screen,(255,100,0), (random.randint(0,600),random.randint(0,600), 20, 20), 1) 
            
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
