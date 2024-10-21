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

clock = pygame.time.Clock()

colors=[blue,red,green,white,black,yellow]
foodx=(random.randint(0,600)//10)*10
foody=(random.randint(0,600)//10)*10
snakex=(random.randint(0,600)//10)*10
snakey=(random.randint(0,600)//10)*10

up=False
down=False
right=False
left=False

snakelist=[]
snakelist.append([snakex,snakey])
#The Game Loop”
while True:
        snakelist.append([snakex,snakey])
        snakelist.pop(0)
        
        screen.fill((255,0,0))
        pygame.draw.rect(screen,yellow, (foodx,foody, 10, 10), 0)
        for segment in snakelist:
             pygame.draw.rect(screen,blue, segment+[10,10])
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                     if up==False:   
                             if event.key == K_DOWN:
                                 down=True
                                 up=False
                                 right=False
                                 left=False
                     if down==False:  
                             if event.key == K_UP:
                                 up=True
                                 down=False
                                 right=False
                                 left=False
                     if right==False:
                             if event.key == K_LEFT:
                                 left=True
                                 up=False
                                 down=False
                                 right=False
                     if left==False:
                             if event.key == K_RIGHT:
                                 right=True
                                 up=False
                                 down=False
                                 left=False
        clock.tick(15)

        #smooth movemement
        if down==True:
                snakey = snakey + 10
                
        if up==True:
                snakey=snakey-10
        if left==True:
                snakex=snakex-10
        if right==True:
                snakex=snakex+10

        #eating food
        if foodx==snakex and foody==snakey:
                foodx=(random.randint(0,600)//10)*10
                foody=(random.randint(0,600)//10)*10
                snakelist.append([foodx,foody])
                print(snakelist)

        #boundary
                
        if snakex==0:
                snakex=590
        if snakey==0:
                snakey=590
        if snakex>=600:
                snakex=0
        if snakey>=600:
                snakey=0
    
        # game over condition

        for i in range(1,len(snakelist)):
                if snakelist[0]==snakelist[i]:
                        pygame.quit()
                        exit()
                        
    #Most of our game logic goes here
    #Continuously update the screen
        pygame.display.update()
