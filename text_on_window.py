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
message=input("Enter your message")

#print(cord)
#The Game Loop”
while True:
    pygame.draw.rect(screen,white, (20,20, 150, 50), 3)
    show_text ("Play",70,40,white,15)

    pygame.draw.rect(screen,white, (300,20, 150, 50), 3)
    show_text ("Quit",370,40,white,15)  

    show_text (message,300,300,yellow,20)   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
