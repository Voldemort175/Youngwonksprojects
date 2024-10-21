#import pygame and initialize the pygame engine.
import pygame
import random
import time
import math
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
colors=[blue,red,green,white,black,yellow]
r=10
cnt=0
xpad1=40
ypad1=250
wpad1=20
hpad1=100
xpad2=540
ypad2=250
wpad2=20
hpad2=100
ballx=300
bally=300

move_up1=False
move_down1=False
move_up2=False
move_down2=False
i=1
j=1
playerblue=0
playerred=0
while True:
    screen.fill((0,0,0))
    time.sleep(0.005)
    pygame.draw.rect(screen,red, (xpad1,ypad1, wpad1, hpad1), 0)
    pygame.draw.rect(screen,blue, (xpad2,ypad2, wpad2, hpad2), 0)
    pygame.draw.circle(screen,yellow, (ballx,bally), 20, 0)
    show_text ("Red Score:",30,40,white,15)
    show_text (str(playerred),120,40,white,15)
    show_text ("Blue Score:",500,40,white,15)
    show_text (str(playerblue),590,40,white,15)

    if playerblue==10:
        show_text ("Player Blue has won",300,250,white,50)
        time.sleep(2)
    if playerred==10:
        show_text ("Player Red has won",300,250,white,50)
        time.sleep(2)
    ballx+=i
    bally+=j
    if (ballx+20)==xpad2:
        if (bally+20)>=ypad2 and (bally-20)<=(ypad2+100):
            i=-1
    if (ballx-20)==xpad1:
        if(bally+20)>=ypad1 and (bally-20)<=(ypad1+100):
            i=1
    if bally<20:
        j=1
    if bally>580:
        j=-1
    if ballx>=580:
        playerred+=1
        ballx=300
    if ballx<=20:
        playerblue+=1
        ballx=300
    if ypad1<=0:
        ypad1=0
    if ypad2<=0:
        ypad2=0
    if ypad1>=500:
        ypad1=500
    if ypad2>=500:
        ypad2=500
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                move_up1=True
            if event.key == K_s:
                move_down1=True
            if event.key == K_UP:
                move_up2=True
            if event.key == K_DOWN:   
                move_down2=True
      
        if event.type == KEYUP:
            if event.key == K_w:
                move_up1=False
            if event.key == K_s:
                move_down1=False
     
            if event.key == K_UP:
                move_up2=False
            if event.key == K_DOWN:
                move_down2=False
    if move_up1:
        ypad1-=2
    if move_down1:
        ypad1+=2
    if move_down2:
        ypad2+=2
    if move_up2:
        ypad2-=2
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()
