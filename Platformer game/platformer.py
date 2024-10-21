import pygame
from pygame.locals import *
screen = pygame.display.set_mode((760,400))
pygame.display.set_caption("Pong!")
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
clock=pygame.time.Clock()

man=pygame.transform.scale(pygame.image.load('Idle__001.png'),(40,40))
    
tile=pygame.transform.scale(pygame.image.load('png\\Tiles\\2.png'),(40,40))

coin=pygame.transform.scale(pygame.image.load('coin.png'),(40,40))


world= [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,1,1],
        [1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1],
        [1,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,1,1],
        [1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1],
        [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

 
coins=[]
collected=[]
up=False
left=False
right=False
jumppossible=False

tiles=[]
gravity=True
jumpvar=1
def collision():
    global gravity
    global jumppossible
    global left
    global right
    global up
    for i in tiles:
        
        if man1.colliderect(i):
            #print(man1.bottom,i.top)
            #print(man1.top,i.bottom)
            #print(man1.left,i.right)
            #print(man1.right,i.left)
            if (man1.bottom-1==i.top):
                gravity=False
                jumppossible=True
            elif (man1.left+1==i.right and i.top+1<man1.bottom):
               left=False
            
            elif (man1.right-1==i.left):
               right=False
            
            elif (man1.top+1==i.bottom or man1.top+2==i.bottom):
                up=False
    for i in coins:
        if man1.colliderect(i):
            x=i.left
            y=i.top
            collected.append((x,y))

##def rewards():
##    global world
##    for k in coins:
##        for i in range(0,10):
##            for j in range(0,20):
##                if world[i][j]==2:
##                    if man1.colliderect(k):
##                        world[i][j]=0
##                        board()
##                        break
                
def board():
    global world
    x=0
    y=0
   

    for i in range(0,10):
        for j in range(0,20):
            if world[i][j]==1:
                tile_print=screen.blit(tile,(x,y))
                tiles.append(tile_print)
            elif world[i][j]==2:
                if (x,y) not in collected:
                    coin_print=screen.blit(coin,(x,y))
                    coins.append(coin_print)
                else:
                    pass
            x+=40
        x=0
        y+=40

    

        
##    for i in range(0,len(layer),1):
##            if layer[i]==1:
##                tile_print=screen.blit(tile,(x,y))
##                tiles.append(tile_print)
##            x+=40
##            
##    layer2=[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
##    x2=40
##    y2=200
##    for i in range(0,len(layer2),1):
##            if layer2[i]==1:
##                tile_print2=screen.blit(tile,(x2,y2))
##                tiles.append(tile_print2)
##            x2+=40
##    return tile_print
manx=40
many=320

while True:
    pygame.display.update()
    screen.fill((0,0,0))
    
    gravity=True
    man1=screen.blit(man,(manx,many))
    board()
    collision()
    #rewards()
    tiletop=board()
##    for i in tilex:
##        for j in tiley:
##            if not(manx==i and many==j-40):
##                many+=20
##                pygame.display.update()
        #print("not collididng")
##    if not man1.colliderect(board()):
##        many+=20
##    else:
##        print("colliding")
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                left=True
                right=False
                up=False
            elif event.key == K_RIGHT :
                right=True
                left=False
                up=False
            elif event.key == K_DOWN:
                print("DOWN KeyPressed")
            elif event.key == K_UP :
                up=True
                
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                left=False
            elif event.key == K_RIGHT :
                right=False
        
    if left==True:
        manx-=1
        pygame.display.update()
    if right==True:
        manx+=1
        pygame.display.update()
            
    if up==True and jumppossible==True:
        many-=jumpvar
        jumpvar+=1
        if jumpvar==16:
            jumppossible=False
            up=False
            jumpvar=0
        
##                
##    if up==True:
##            if jumpvar<6:
##                y-=15
##            elif jumpvar>=6:
##                y+=15
##            screen.fill((255,255,255))
##            jump_action=screen.blit(jump[jumpvar],(100,y))
##            if jumpvar==9:
##                up=False
##                y=300
##                jumpvar=0
##            jumpvar+=1
##    n+=1
##    
##    if n==10:
##        n=0
##
    if gravity==True:
        many+=1
    clock.tick(150)
