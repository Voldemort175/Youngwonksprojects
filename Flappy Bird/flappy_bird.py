#import pygame and initialize the pygame engine.
import pygame
from pygame.locals import *
import time
import random
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

red=(255,0,0)

bg=pygame.image.load('bg.png')
bg=pygame.transform.scale(bg,(600,600))
pygame.image.load('bird.png')
bird=pygame.image.load('bird.png')
bird=pygame.transform.scale(bird,(40,40))

pygame.image.load('pipe.png').convert()
pipe=pygame.image.load('pipe.png')
pipe=pygame.transform.scale(pipe,(150,200))    #bottom
pipe2=pygame.transform.flip(pipe,False,True)
pipe2=pygame.transform.scale(pipe2,(150,200))  #top
#The Game Loop”
birdx=300
birdy=300
pipex=400
pipey=400
pipe2x=400
pipe2y=0

score=0

while True:
    pipechange=random.randint(100,350)
    screen.fill((0,0,0))
    bg2=screen.blit(bg,(0,0))
    bird3=screen.blit(bird,(birdx,birdy))
    pipe3=screen.blit(pipe,(pipex,pipey))
    pipe4=screen.blit(pipe2,(pipe2x,pipe2y))
    show_text("Score=",40,40,(0,0,0),20)
    show_text(str(score),95,40,(0,0,0),20)
    pipex-=1
    pipe2x-=1

    if bird3.colliderect(pipe3) or bird3.colliderect(pipe4):
        show_text("GAME OVER",300,300,(0,0,0),50)
        time.sleep(2)
    if (pipex-2)<0 and (pipe2x-2)<0:
        pipe2=pygame.transform.scale(pipe2,(150,pipechange))
        pipe=pygame.transform.scale(pipe,(150,350-pipechange+200))
        pipey=pipechange+200
        
        pipex=550
        pipe2x=550
    
    birdy+=1
    if birdx==(pipex+160):    # score condition
        score+=1
        print(score)
    if birdy==560:
        time.sleep(2)
        show_text ("GAME OVER",70,40,red,15)
        time.sleep(2)
    if birdy==0:
        show_text ("GAME OVER",70,40,red,15)
        time.sleep(2)
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:      #  hit a key
            if event.key==K_SPACE:
                birdy-=30 
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
