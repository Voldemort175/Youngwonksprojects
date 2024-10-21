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
twink=[white,yellow]
cord=[]
for i in range(0,100):
        x=random.randint(0,600)
        y=random.randint(0,600)
        j=[x,y]
        cord.append(j)
#print(cord)
while True:
    screen.fill((0,0,0))
    time.sleep(0.1)
    for i in cord:
        pygame.draw.circle(screen,random.choice(twink),i,3,2)
        i[1]+=1    
        if i[1]==600:
            i[1]=0
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
