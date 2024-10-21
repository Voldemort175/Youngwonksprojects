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
x_1=0
y_1=0
x_2=540

while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(r,g,b), (x_1,y_1, 60, 60), 0)
    x_1+=60
    pygame.draw.rect(screen,(r,g,b), (x_2,y_1, 60, 60), 0)
    x_2-=60
    y_1+=60
    time.sleep(0.15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
