#import pygame and initialize the pygame engine.
import pygame
from pygame.locals import *
import time
import random
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((640,480))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
#The Game Loop”
x=0
y=0
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

while True:
    
    #pygame.draw.circle(screen,(0,255,0), (320, 240), 100, 2) # for drawing a circle
    #pygame.draw.rect(screen,(255,100,0), (20,20, 150, 50), 3)
    #pygame.draw.line(screen, (255,100,0), (50,50),(100,100),2)
    #pygame.draw.line(screen, (255,100,0), (100,50),(50,50),2)
    #pygame.draw.line(screen, (255,100,0), (100,50),(100,100),2)
    #pygame.draw.polygon(screen,(0,255,255), ((50,50),(100,50),(100,100)),5)# polygon of any number of points

    #corner rectangles
    #pygame.draw.rect(screen,(255,100,0), (0,0, 150, 50), 3)
    #pygame.draw.rect(screen,(255,100,0), (490,430, 150, 50), 3)

    #pattern
    '''
    pygame.draw.circle(screen,(255,55,0), (0,0),100,0)
    pygame.draw.circle(screen,(255,55,0), (640,0),100,0)
    pygame.draw.circle(screen,(255,55,0), (0,480),100,0)
    pygame.draw.circle(screen,(255,55,0), (640,480),100,0)
    pygame.draw.circle(screen,(255,55,0), (320,240),100,0)
    '''

    # x pattern
    '''
    pygame.draw.line(screen,(0,0,255),(0,0),(640,480),1)
    pygame.draw.line(screen,(0,0,255),(640,0),(0,480),1)
    '''

    #grid pattern
    '''
    for x_p in range(0,640,64):
        pygame.draw.line(screen,(0,255,0),(x_p,0),(x_p,480),1)
    for y_p in range(0,480,48):
        pygame.draw.line(screen,(0,255,0),(0,y_p),(640,y_p),1)
    '''
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(r,g,b), (x,y, 40, 40), 0)
    x+=40
    time.sleep(0.15)
    if x==640:
        x=0
        y+=40
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
