#import pygame and initialize the pygame engine.
import pygame
import random
import time
from pygame.locals import *
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((600,600))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
#The Game Loop”


x_circ=300
y_circ=350
x_rect=250
while True:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,100,0), (x_rect,300, 150, 50), 0)
    pygame.draw.circle(screen,(0,255,0), (x_circ, y_circ), 10, 0)
    x_circ+=20
    x_rect+=20
    time.sleep(0.15)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
