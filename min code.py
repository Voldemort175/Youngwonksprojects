#import pygame and initialize the pygame engine.
import pygame
from pygame.locals import *
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((640,480))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
#The Game Loop”
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            print(chr(event.key))
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
