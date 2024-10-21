import random
import time

class circle():
    radius=25
    def __init__(self):
        self.x=random.randint(1,500)
        self.y=random.randint(1,500)
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.direction=random.choice(["left","right"])
        self.speed = random.randint(1,4)
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

    def move(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
        if self.x>=600 and self.direction=="right":
            self.x=0
            self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if self.x<=0 and self.direction=="left":
            self.x=600
            self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if self.direction=="left":
            self.x-=self.speed
        else:
            self.x+=self.speed
import pygame
from pygame.locals import *
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((600,600))
#To set the name of our window to “Shapes”
#The Game Loop”
l=[]
for i in range(30):
     x=circle()
     l.append(x)
# print(l)
i=0   
while i<30:
     l[i].draw()
     i+=1
i=0
screen.fill((0,0,0))
while True:
    time.sleep(0.004)
    screen.fill((0,0,0))
    for i in range(30):
        l[i].move()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Most of our game logic goes here
    #Continuously update the screen
    pygame.display.update()


