import pygame, random
from pygame.locals import *
from tkinter import *
root=Tk()
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((600,600))

qmark=pygame.image.load("D:\\Study Stuff\\Wonksknow\\level 3 oops\\Tkinter\\9.png")
qmark=pygame.transform.scale(qmark,(50,50))
pygame.image.save(qmark,"D:\\Study Stuff\\Wonksknow\\level 3 oops\\Tkinter\\9.png")

imagelist=[]

for i in range(1,9):
    img=pygame.image.load(f"D:\\Study Stuff\\Wonksknow\\level 3 oops\\Tkinter\\{i}.png")
    img=pygame.transform.scale(img,(50,50))
    pygame.image.save(img,f"D:\\Study Stuff\\Wonksknow\\level 3 oops\\Tkinter\\{i}.png")
    img1=PhotoImage(file=f"D:\\Study Stuff\\Wonksknow\\level 3 oops\\Tkinter\\{i}.png")
    img2=PhotoImage(file=f"D:\\Study Stuff\\Wonksknow\\level 3 oops\\Tkinter\\{i}.png")
    imagelist.append(img1)
    imagelist.append(img2)
numlist=[]
for i in range(1,9):
    numlist.append(i)
    numlist.append(i)
print(numlist)
for i in range(0,len(imagelist)):
    imagelist[i]=(imagelist[i],numlist[i])
print(imagelist)
random.shuffle(imagelist)
qmark=PhotoImage(file="D:\\Study Stuff\\Wonksknow\\level 3 oops\\Tkinter\\9.png")