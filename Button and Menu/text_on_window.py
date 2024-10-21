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
turn = "x"
gridx=0
gridy=0
dict={
    "1":"","2":"","3":"",
    "4":"","5":"","6":"",
    "7":"","8":"","9":""
    }
def win():
    global chance
    global dict
    if dict["1"] == dict["2"] == dict["3"] !="":
        show_text( dict["1"] + ' Wins!', 300, 300, red, 45 )
        pygame.display.update()
        time.sleep(3)
    elif dict["4"] == dict["5"] == dict["6"] !="":
        show_text( dict["4"] + ' Wins!', 300, 300, red,45 )
        pygame.display.update()
        time.sleep(3)
    elif dict["7"] == dict["8"] == dict["9"] !="":
        show_text( dict["7"] + ' Wins!', 300, 300, red, 45 )
        pygame.display.update()
        time.sleep(3)
    elif dict["4"] == dict["5"] == dict["6"] !="":
        show_text( dict["4"] + ' Wins!', 300, 300, red, 45 )
        pygame.display.update()
        time.sleep(3)
    elif dict["1"] == dict["4"] == dict["7"] !="":
        show_text( dict["1"] + ' Wins!', 300, 300, red, 45 )
        pygame.display.update()
        time.sleep(3)
    elif dict["2"] == dict["5"] == dict["8"] !="":
        show_text( dict["2"] + ' Wins!', 300, 300, red, 45 )
        pygame.display.update()
        time.sleep(3)
    elif dict["3"] == dict["6"] == dict["9"] !="":
        show_text( dict["3"] + ' Wins!', 300, 300, red, 45 )
        pygame.display.update()
        time.sleep(3)
    elif dict["1"] == dict["5"] == dict["9"] !="":
        show_text( dict["1"] + ' Wins!', 300, 300, red, 45 )
        pygame.display.update()
        time.sleep(3)
    elif dict["3"] == dict["5"] == dict["7"] !="":
        show_text( dict["3"] + ' Wins!', 300, 300, red, 45 )
        pygame.display.update()
        time.sleep(3)
    elif chance==9:
        show_text( ' Tie! GAME OVER', 300, 300, red, 45 )
        pygame.display.update()
        time.sleep(3)
        
block="0"
chance=0
def game():
        screen.fill((0,0,0))
        
        global gridx
        global gridy
        global turn
        global block
        global chance
        global dict
        print(dict)
        while True:
                for j in range(0,3):
                        for i in range(0,9):
                            pygame.draw.rect(screen,yellow,(gridx,gridy, 200,200),2)    #grid
                            gridx+=200
                        gridy+=200
                        gridx=0
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()

                        if event.type == MOUSEBUTTONDOWN:
                            chance+=1
                            x1,y1=event.pos
                            
                            
                            if 0<x1<200 and 0<y1<200:       #1
                                x1,y1=0,0
                                block="1"
                            if 200<x1<400 and 0<y1<200:     #2
                                x1,y1=200,0
                                block="2"
                            if 400<x1<600 and 0<y1<200:     #3
                                x1,y1=400,0
                                block="3"
                            if 0<x1<200 and 200<y1<400:     #4
                                x1,y1=0,200
                                block="4"
                            if 200<x1<400 and 200<y1<400:   #5
                                x1,y1=200,200
                                block="5"
                            if 400<x1<600 and 200<y1<400:   #6
                                x1,y1=400,200
                                block="6"
                            if 0<x1<200 and 400<y1<600:     #7
                                x1,y1=0,400
                                block="7"
                            if 200<x1<400 and 400<y1<600:   #8
                                x1,y1=200,400
                                block="8"
                            if 400<x1<600 and 400<y1<600:   #9
                                x1,y1=400,400
                                block="9"
                            x2=x1+200
                            y2=y1+200
                            if turn =="x":
                                if(dict[block]==""):
                                    dict[block]="x"
                                    pygame.draw.line(screen,white,(x1,y1),(x2,y2),2)
                                    pygame.draw.line(screen,white,(x2,y1),(x1,y2),2)
                                    win()
                                    turn="o"
                                else:
                                    break
                                
                                break
                            if turn=="o":
                                if(dict[block]==""):
                                    dict[block]="o"
                                    pygame.draw.circle(screen,white,((x1+x2)/2,(y1+y2)/2),50,2)
                                    win()
                                    turn="x"
                                else:
                                    break


#print(cord)
#The Game Loop”
def menu():
        while True:
            pygame.draw.rect(screen,green, (20,180, 150, 50), 3)
            show_text ("Play",70,200,white,15)

            pygame.draw.rect(screen,white, (300,180, 150, 50), 3)
            show_text ("Quit",370,200,white,15)  

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                        x,y=event.pos
                        if 20<x<170 and 180<y<230:
                                print("Play")
                                
                                game()
                        elif 300<x<450 and 180<y<230:
                                pygame.quit()
                                exit()
                                
            #Most of our game logic goes here
            #Continuously update the screen
            pygame.display.update()
menu()
