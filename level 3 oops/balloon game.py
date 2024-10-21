import random
import time
import pygame 



def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("arial", size, bold=True, italic=True)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))

class balloon():
    def __init__(self):
        self.x=random.randint(0,500)
        self.y=600
        self.balimg=pygame.image.load("D:\\Study Stuff\\Wonksknow\\level 3 oops\\balloon.jpg")
        self.balimg=pygame.transform.scale(self.balimg,(100,200))
        self.letter= chr(random.randint(97,122))
        
    def show(self):
        screen.blit(self.balimg, (self.x,self.y))
        show_text(self.letter,self.x+45,self.y+30,(255,255,255),30)
        self.y-=2
        time.sleep(0.05)

import pygame
from pygame.locals import *
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((600,600))
balloonlist=[]
balloonlist.append(balloon())

while True:
    screen.fill((0,0,0))
    for i in balloonlist: 
        i.show()
        # if i.y<0:
        #     balloonlist.remove(i)
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            wrong_key=True
            for i in balloonlist:
                if event.unicode == i.letter:
                    # print("popped")
                    balloonlist.remove(i)
                    del i
                    balloonlist.append(balloon())  
                    wrong_key=False
                    break
                    
            if wrong_key:
                balloonlist.append(balloon())  

                    
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
