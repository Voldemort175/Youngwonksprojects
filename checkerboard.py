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

def board():

    x_rect=0
    y_rect=0
    blue=(0,0,255)
    red=(255,0,0)
    green=(0,255,0)
    white=(255,255,255)
    black=(0,0,0)
    yellow=(255,255,0)
    colors=[blue,red,green,white,black,yellow]
    while True:
        #screen.fill((0,0,0))
        for y_rect in range(0,551,50):
            #red,blue=blue,red
            for x_rect in range(0,551,50):
                pygame.draw.rect(screen,random.choice(colors), (x_rect,y_rect, 50, 50), 0)
                #red,blue=blue,red
                #time.sleep(0.15)
            
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        #Most of our game logic goes here
        #Continuously update the screen
        pygame.display.update()

board()
