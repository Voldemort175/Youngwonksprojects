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
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("arial", size, bold=True, italic=True)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))

#The Game Loop”
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
white=(255,255,255)
black=(0,0,0)
yellow=(255,255,0)
x_circ=300
y_circ=300
j=""
l=[]
shift=300
while True:
    screen.fill((0,0,0))
    print(l)
    for i in range(0,len(l)):
        show_text (l[i],shift,300,white,15)
        shift+=10
        time.sleep(1)
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            l.append(chr(event.key))
        if event.type == MOUSEBUTTONDOWN:
            print(event.button,event.pos)
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
