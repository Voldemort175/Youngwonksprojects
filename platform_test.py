import pygame
import time
pygame.init()
from pygame.locals import *
screen = pygame.display.set_mode((1280,768))
pygame.display.set_caption("Hello!!")
sprite=pygame.image.load("D:\\Study Stuff\\Wonksknow\\Pygame\\Platformer game\\Idle__000.png")
sprite=pygame.transform.scale(sprite,(80,128))
jump=[]
run=[]
for un in range(0,10):
    path=f"D:\Study Stuff\Wonksknow\Pygame\Platformer game\Run__00{un}.png"
    mat=pygame.image.load(path)
    mat=pygame.transform.scale(mat,(100,138))
    run.append(mat)
for a in range(0,10):
    path=f"D:\Study Stuff\Wonksknow\Pygame\Platformer game\Jump__00{a}.png"
    hat=pygame.image.load(path)
    hat=pygame.transform.scale(hat,(100,138))
    jump.append(hat)

x=500
y=100
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
player=screen.blit(screen,(300,50))
direction='right'
tiles={}
tiles[1]=pygame.image.load("D:\\Study Stuff\\Wonksknow\\Pygame\\Platformer game\\png\\Tiles\\2.png")
tiles[1]=pygame.transform.scale(tiles[1],(128,128))
Level_1=[[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1],
        [0,0,0,1,1,1,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1]]
collidables=[1]
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
            if column!=0:
                screen.blit(tiles[column],(j*128,i*128))
get_rects(Level_1)
while True:
    player_rect=pygame.draw.rect(screen,(0,0,0),(x,y,80,128))
    # play=screen.blit(sprite, (x,y))                                  # no need to draw sprite twice
    screen.fill((0,0,0))
    draw_level(Level_1)
    hits=player_rect.collidelistall(rects)
    if ground==False:
        y=y+16
        player_rect.x = x                                            # update player_rect everywhere
        player_rect.y = y
        if direction=='right':
            player=screen.blit(jump[6],(x,y))
        if direction=='left':
            img=pygame.transform.flip(jump[6],1,0) 
            player=screen.blit(img,(x,y))                            # change img[6] -> to img
    if len(hits)>0:
        for i in hits:
            if rects[i].collidepoint(player_rect.midbottom):                    # use player rect
                y=rects[i].top-player_rect.height+1                          #change playerY to y and use player rect
                ground=True
                print(hits)
            else:
                ground=False
    else:
        ground=False
    if direction=='right':
        if x==0 and ground:
            player=screen.blit(sprite,(x,y))
        if x!=0 and ground:
            player=screen.blit(run[frame//2],(x,y))
        if hop:
            player=screen.blit(jump[frame//2],(x,y))
        if not jump and not ground:
            player=screen.blit(jump[-1],(x,y))
    if direction=='left':
        if x==0 and ground:
            sprite=pygame.transform.flip(sprite[frame],1,0)
            Lrun=True
        if x!=0 and ground:
            img=pygame.transform.flip(run[frame//2],1,0)
            player=screen.blit(img,(x,y))
        if hop:
            bjump=pygame.transform.flip(jump[frame//2],1,0)
            player=screen.blit(bjump,(x,y))
        if not jump and not ground:
            player=screen.blit(bjump[-1],(x,y))
    if hop==True:
        # if b==0:
        #     y=y-10                                    # no need for this
        frame=(frame+1)%10
        if direction=='right':
            player=screen.blit(jump[frame],(x,y))
        if 0<=b<=4:
            y=y-64
        if 5<=b<=10:                                    # need to add condition for going down
            y=y+64
        b=b+1
        player_rect.x = x
        player_rect.y = y
        time.sleep(0.005)
        pygame.display.update()
    if b==10:
        hop=False
    if Lrun==True: 
        frame=(frame+1)%10
        pygame.display.update()
        x=x-30
        player_rect.x = x
        player_rect.y = y
        time.sleep(0.005)
    if Run==True: 
        frame=(frame+1)%10
        pygame.display.update()
        x=x+30
        player_rect.x = x
        player_rect.y = y
        time.sleep(0.005)
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
            exit()                                          # add exit for proper exit
    clock.tick(25)
    pygame.display.update()