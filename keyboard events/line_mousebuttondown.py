#import pygame and initialize the pygame engine.
import pygame
import random
from pygame.locals import *
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((600,600))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
#The Game Loop”
isrect=False
line=[]
while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            x,y=event.pos
            line.append(x)
            line.append(y)
            if len(line)==4:
                pygame.draw.line(screen, (255,100,0), (line[0],line[1]),(line[2],line[3]),3)
                
##        if event.type == MOUSEMOTION:
##            x_circ , y_circ = event.pos
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
