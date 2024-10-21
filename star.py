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



x_rect=0
y_rect=0
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
white=(255,255,255)
black=(0,0,0)
yellow=(255,255,0)
colors=[blue,red,green,white,black,yellow]
cord=[(300,200),(150,300),(450,300),(225,450),(375,450)]
while True:
    pygame.draw.line(screen,(random.choice(colors)),cord[0],cord[3],2)
    pygame.draw.line(screen,(random.choice(colors)),cord[0],cord[4],2)
    pygame.draw.line(screen,(random.choice(colors)),cord[1],cord[2],2)
    pygame.draw.line(screen,(random.choice(colors)),cord[1],cord[4],2)
    pygame.draw.line(screen,(random.choice(colors)),cord[2],cord[3],2)
   
   
   
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
