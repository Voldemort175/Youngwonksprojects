import pygame
import time
pygame.init()
from pygame.locals import *
screen = pygame.display.set_mode((1280,768))
pygame.display.set_caption("Hello!!")
sprite=pygame.image.load('D:\\Study Stuff\\Wonksknow\\Pygame\\Platformer game\\Idle__000.png')
sprite=pygame.transform.scale(sprite,(80,128))
jump=[]
run=[]
coinobj=[]
for un in range(0,10):
    path=f'D:\Study Stuff\Wonksknow\Pygame\Platformer game\Run__00{un}.png'
    mat=pygame.image.load(path)
    mat=pygame.transform.scale(mat,(100,138))
    run.append(mat)
for a in range(0,10):
    path=f'D:\Study Stuff\Wonksknow\Pygame\Platformer game\Jump__00{a}.png'
    hat=pygame.image.load(path)
    hat=pygame.transform.scale(hat,(100,138))
    jump.append(hat)
x=0
y=256
frame=0
framer=0
clock=pygame.time.Clock()
hop=False
Lrun=False
Run=False
Left=False
rects=[]
ground=True
def show_text(msg,w,z, color, size):
    fontobj= pygame.font.SysFont("arial", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(w, z))
b=0
player=screen.blit(screen,(300,256))
direction='right'
tiles={}
tiles[1]=pygame.image.load("D:\\Study Stuff\\Wonksknow\\Pygame\\Platformer game\\png\\Tiles\\2.png")
tiles[1]=pygame.transform.scale(tiles[1],(128,128))
Level_1=[[0,0,0,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,0,1,1,1],
        [0,0,0,1,1,1,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0]]
collidables=[1]
doorpos=[2]
coinpos=[[4,1],[4,1],[0,8]]
door=[]
money=0
def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont("comicsans", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))
def get_rects(level):
    for i,row in enumerate(level):
        for j,column in enumerate(row):
            if column in collidables:
                rect=pygame.Rect(j*128,i*128,128,128)
                if rect not in rects:
                    rects.append(rect)
def draw_level(level):
    for i,row in enumerate(level):
        for j, column in enumerate(row):
            if column==1:
                screen.blit(tiles[column],(j*128,i*128))
            elif column==2:
                doorpos=pygame.draw.rect(screen,(117, 57, 11),(j*128,i*128,80,128))
                door.append(doorpos)
get_rects(Level_1)
def draw_coins(row,col):
    global coinobj
    coin=pygame.draw.circle(screen,(252, 186, 3),(row*128+32,col*128+32),32)
    if coin not in coinobj:
        coinobj.append(coin)
while True:
    playerRect=pygame.draw.rect(screen,(0,0,0),(x,y,80,128))
    screen.fill((0,0,0))
    draw_coins(coinpos[0][0],coinpos[0][1])
    draw_level(Level_1)
    hits=playerRect.collidelistall(rects)
    dooropen=player.collidelistall(door)
    if y>=768:
        screen.fill((0,0,0))
        show_text("LOSE",560,200,(255,255,255),100)
        show_text("MONEY $"+str(money),600,380,(252, 186, 3),32)
        pygame.display.update()
        pygame.quit()
        exit()
    if len(dooropen)!=0:
        screen.fill((0,0,0))
        show_text("WIN",560,200,(255,255,255),100)
        show_text("MONEY $"+str(money-1),600,380,(252, 186, 3),32)
        pygame.display.update()
        pygame.quit()
        exit()
    cointouch=player.collidelistall(coinobj)
    if len(cointouch)!=0:
        money=money+1
        coinpos.pop(cointouch[0])
        coinobj.pop(cointouch[0])
        cointouch.pop()
    if ground==False and hop==False:
        if y<768 - playerRect.height:
            y=y+16
        else:
            ground=True
        playerRect.x=x
        playerRect.y=y
        if direction=='right':
            playerRect=screen.blit(jump[6],(x,y))
        if direction=='left':
            img=pygame.transform.flip(jump[6],1,0)
            playerRect=screen.blit(img,(x,y))
    if len(hits)>0:
        for i in hits:
            if rects[i].collidepoint(playerRect.midbottom):
                y=rects[i].top-playerRect.height+1
                ground=True
            else:
                ground=False
    else:
        ground=False
    if direction=='right':                          # make changes
        if ground:
            if Run:
                player=screen.blit(run[frame//2],(x,y))
            else:
                player=screen.blit(sprite,(x,y))     
        if not jump and not ground:
            player=screen.blit(jump[-1],(x,y))
    if direction=='left':
        if ground:
            sprite=pygame.transform.flip(sprite,1,0)
        if ground:
            img=pygame.transform.flip(run[frame//2],1,0)
            player=screen.blit(img,(x,y))
        if hop:
            bjump=pygame.transform.flip(jump[frame//2],1,0)
            player=screen.blit(bjump,(x,y))
        if not jump and not ground:
            player=screen.blit(bjump[-1],(x,y))
    if hop==True:
        frame=(frame+1)%10
        if direction=='right':
            player=screen.blit(jump[frame],(x,y))
        if 0<=b<=4:
            y=y-36
        elif 5<=b<10:
            y=y+36
        b=b+1
        playerRect.x=x
        playerRect.y=y
        time.sleep(0.05)
        pygame.display.update()
    if b==10:
        hop=False
    if Lrun==True: 
        frame=(frame+1)%10
        pygame.display.update()
        x=x-20
        playerRect.x=x
        playerRect.y=y
        time.sleep(0.05)
    if Run==True: 
        frame=(frame+1)%10
        pygame.display.update()
        x=x+20
        playerRect.x=x
        playerRect.y=y
        time.sleep(0.05)
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                hop=True
                b=0
            if event.key==K_LEFT:
                direction='left'
                Lrun=True
            if event.key==K_RIGHT:
                direction='right'
                Run=True                     
        if event.type==KEYUP:
            Lrun=False
            Run=False
        if event.type == QUIT:
            pygame.quit()
            exit()
    clock.tick(25)
    pygame.display.update()