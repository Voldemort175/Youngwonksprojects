#import pygame and initialize the pygame engine.
import pygame
import random
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
x_circ=300
y_circ=300
while True:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,color, (x_circ,y_circ),30,0)
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if event.type == MOUSEBUTTONDOWN:
            print(event.button,event.pos)
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
