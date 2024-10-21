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
color=(0,255,0)
x=0
y=0
while True:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,color,(300,200,50,100), 0)
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            x,y=event.pos
            if 300<=x<=350 and 200<=y<=300:
                color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                
            print(x,y)
##        if event.type == MOUSEMOTION:
##            x_circ , y_circ = event.pos
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
