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



x1=50
flag1=5
x2=550
flag2=5
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
    screen.fill((0,0,0))
    pygame.draw.circle(screen,white,(x1,300),25,0)
    pygame.draw.circle(screen,yellow,(x2,300),25,0)
    x1+=flag1
    x2-=flag2
    time.sleep(0.05)
    if x1==275:
        flag1=-5
    if x1==25:
        flag1=5
    if x2==325:
        flag2=-5
    if x2==575:
        flag2=5
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
