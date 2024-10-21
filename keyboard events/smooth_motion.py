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
x_circ=300
y_circ=300

move_left= False
move_right=False
move_up=False
move_down=False

while True:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,color, (x_circ,y_circ),30,0)
    time.sleep(0.1)
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            #if move_left==False:
                if event.key == K_RIGHT:
                    move_right=True
                    move_left= False
                    move_up=False
                    move_down=False    
           # if move_right==False:
                if event.key == K_LEFT:
                    move_left=True
                    move_right=False
                    move_up=False
                    move_down=False
            #if move_down==False:        
                if event.key == K_UP:
                    move_up=True
                    move_left= False
                    move_right=False
                    move_down=False
            #if move_up==False:        
                if event.key == K_DOWN:
                    move_down=True
                    move_left= False
                    move_right=False
                    move_up=False
            
##            if (event.key == K_UP and event.key == K_RIGHT):
##                y_circ-=0
##                x_circ+=0
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                move_right=False
            if event.key == K_LEFT:
                move_left=False
            if event.key == K_UP:
                move_up=False
            if event.key == K_DOWN:
                move_down=False
    if move_right==True:
        x_circ+=10
    if move_left==True:
        x_circ-=10
    if move_up==True:
        y_circ-=10
    if move_down==True:
        y_circ+=10
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
