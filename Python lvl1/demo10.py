import pygame
import time
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!")
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
color=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
while True:
    pygame.display.update()
    for event in pygame.event.get():
        pygame.draw.rect(screen,(255,255,255),(0,0,20,20))
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEBUTTONDOWN:
            time.sleep(0.33333333333)
            if event.type==MOUSEBUTTONDOWN:
                for i in range(0,51,1):
                    if event.pos[0]==i:
                        for a in range(0,51,1):
                            if event.pos[1]==a:
                                pygame.draw.rect(screen,(255,255,255),(random.randint(1,550),random.randint(1,550),20,20))
