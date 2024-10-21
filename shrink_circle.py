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

r=50
R=random.randint(0,255)
G=random.randint(0,255)
B=random.randint(0,255)
check=10
while True:
    screen.fill((0,0,0))
    if r<=600:
        pygame.draw.circle(screen,(R,G,B), (300, 300), r, 0)
        time.sleep(0.05)
        r+=check
    if r==300:
        check=-10
        R=random.randint(0,255)
        G=random.randint(0,255)
        B=random.randint(0,255)
    if r==10:
        check=10

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
