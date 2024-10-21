import pygame
import time
pygame.init()
from pygame.locals import *
screen = pygame.display.set_mode((1280,768))
pygame.display.set_caption("Hello!!")
sprite=pygame.image.load('/Users/lcmpmac/Downloads/png/Idle__000.png')
sprite=pygame.transform.scale(sprite,(100,200))
jump=[]
run=[]
RRRun=[]
for lun in range(0,10):
    path=f'/Users/lcmpmac/Downloads/png/Run__00{lun}.png'
    mat=pygame.image.load(path)
    mat=pygame.transform.flip(mat,True,False)
    mat=pygame.transform.scale(mat,(150,200))
    run.append(mat)
for un in range(0,10):
    path=f'/Users/lcmpmac/Downloads/png/Run__00{un}.png'
    mat=pygame.image.load(path)
    mat=pygame.transform.scale(mat,(150,200))
    RRRun.append(mat)
for a in range(0,10):
    path=f'/Users/lcmpmac/Downloads/png/Jump__00{a}.png'
    hat=pygame.image.load(path)
    hat=pygame.transform.scale(hat,(150,250))
    jump.append(hat)
x=300
y=300
frame=0
framer=0
clock=pygame.time.Clock()
hop=False
Lrun=False
Run=False
Left=False
def show_text(msg,w,z, color, size):
    fontobj= pygame.font.SysFont("arial", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(w, z))
while True:
    screen.fill((0,0,0))
    circle=pygame.draw.circle(screen,((255,255,255)),(900,300),30)
    rect=pygame.draw.rect(screen,((0,0,0)),(x,y,110,200))
    if rect.colliderect(circle):
        screen.fill((0,0,0))
        show_text("GAME OVER!",540,384,(255,0,0),32)
        pygame.display.update()
        pygame.quit()
        exit()
    if hop==True:
        y=y-20
        for b in range(0,10):
            frame=(frame+1)%10
            screen.blit(jump[frame],(x,y))
            if 0<=b<=5:
                y=y-10
            else:
                y=y+20
            time.sleep(0.05)
            pygame.display.update()
            screen.fill((0,0,0))
        hop=False
    if Lrun==True: 
        frame=(frame+1)%10
        screen.blit(run[frame],(x,y))
        pygame.display.update()
        x=x-10
        time.sleep(0.05)
    if Run==True: 
        frame=(frame+1)%10
        screen.blit(RRRun[frame],(x,y))
        pygame.display.update()
        x=x+10
        time.sleep(0.05)
    if Lrun==False and Run==False:
        screen.blit(sprite,(x,300)) 
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                hop=True
            if event.key==K_LEFT:
                Lrun=True
            if event.key==K_RIGHT:
                Run=True
        if event.type==KEYUP:
            Lrun=False
            Run=False
        if event.type == QUIT:
            pygame.quit()
    clock.tick(25)
    pygame.display.update()
