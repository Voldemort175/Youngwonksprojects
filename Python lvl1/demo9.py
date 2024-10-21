import pygame
from pygame.locals import *
pygame.init()
clock= pygame.time.Clock()
def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont('calibri', 32)
    msgobj = fontobj.render(msg,False,color, size)
    screen.blit(msgobj,(x, y))
screen = pygame.display.set_mode((840,600))
pygame.display.set_caption("My game")
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)
pink = (200,0,200)
orange = (240,100,0)
yellow = (235,225,0)
black = (0,0,0)
white = (255,255,255)
layers = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,1,0,1,0,1,0,1,0,1,0,1,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,0,1,0,1,0,1,0,1,0,1,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,1,1,1,1,1,0,0,1,1,1,0,1],
          [1,0,0,0,0,0,0,0,0,1,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
runflagleft = 0
runflagright = 0
dinox = 60
dinoy = 450
tilex = 0
tiley = 0
coinx = 60
coiny = 60
tilelist = []
jumpflag = 0
jumping = 0
isjump = 0
dinoog = pygame.image.load("Run (2).png")
dino = pygame.transform.scale(dinoog,(50,50))
tileog = pygame.image.load("10.png")
tile = pygame.transform.scale(tileog,(60,60))
##coinog = pygame.image.load("coin.png")
##coin = pygame.transform.scale(coinog,(50,50))
while True:
    screen.fill(black)
    gravity = True
    for i in layers:
        for j in i:
            if j ==1:
                tilesprite = screen.blit(tile,(tilex,tiley)) 
                tilelist.append(tilesprite)
##            elif j == 2:
##                 coinsprite = screen.blit(coin,(tilex,tiley))
            tilex = tilex+60
            if tilex == 840:
                tilex = 0 
        tiley = tiley+60
        if tiley == 600:
             tiley = 0
    character = screen.blit(dino,(dinox,dinoy))
    # if character.colliderect(tilesprite):
    #     print("hello")
    for i in tilelist:    
        if character.colliderect(i):
            #print(character.bottom-1,i.top)
            if character.bottom-1== i.top or character.bottom-12==i.top:
                gravity = False
                isjump = 1
            # if character.top + 8 == i.bottom:
            #     jumpflag = 0
            if character.left+2 == i.right and i.top+1 < character.bottom:
                runflagleft = 0
                gravity = True
            if character.right - 2==i.left and i.top + 1<character.bottom:
                runflagright = 0               
                gravity = True
            if character.top+3== i.bottom:
                gravity = False
                #  character.right == i.left:
    if runflagright != 0 or runflagleft != 0:
        sprite = screen.blit(dino,(dinox,dinoy))
        if runflagright!=0:
            dinox = dinox + 2
        else:
            dinox = dinox - 2
    elif jumpflag == 1:
        screen.blit(dino,(dinox,dinoy))
        jumping = jumping + 1
        if jumping<11 and jumpflag == 1:
            dinoy = dinoy -16
            clock.tick(45)
        if jumping>10 and jumpflag == 1:
             dinoy = dinoy +11
             clock.tick(45)
        if jumping == 21:
            jumpflag = 0
            jumping = 0
            isjump = 0 
    elif (runflagright == 1 and jumpflag == 1)or (runflagleft == 1 and jumpflag == 1):
        print("new condition")
        screen.blit(dino,(dinox, dinoy))
        jumping = jumping + 1
        if jumping<11 and jumpflag == 1:
            dinoy = dinoy -16
            clock.tick(45)
        if jumping>10 and jumpflag == 1:
             dinoy = dinoy +11
             clock.tick(45)
        if jumping == 21:
            jumpflag = 0
            jumping = 0
            isjump = 0 
        if runflagright!=0:
            dinox = dinox + 2
        else:
            dinox = dinox - 2
    if gravity == True:
        dinoy = dinoy+1
    # for i in tilelist:
    #     # if i.colliderect(character):
    #     #      print(character.top,i.bottom)
    #     if character.top +8 >= i.bottom:
    #         print(i.left,i.top)
             
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_UP:
##                        print('up key pressed')
            if event.key == pygame.K_UP and isjump == 1:
                    jumpflag = 1
            if event.key == pygame.K_LEFT:
                    runflagleft = 1
                    isjump = 1
            if event.key == pygame.K_RIGHT:
                    runflagright = 1
                    isjump = 1
        if event.type == pygame.KEYUP:
##                if event.key == pygame.K_UP:
##                        print('up key released')
            # if event.key == pygame.K_SPACE:
                    # jumpcounter
            if event.key == pygame.K_LEFT:
                    runflagleft = 0
            if event.key == pygame.K_RIGHT:
                    runflagright = 0
##          if event.type == pygame.MOUSEMOTION:
##                print(event.pos)
##          if event.type == pygame.MOUSEBUTTONDOWN:
##                if event.button == 1:
##                        print('left button pressed', event.pos)
##        if event.type == pygame.MOUSEBUTTONUP:
##                if event.button == 1:
##                        print('left button released', event.pos)
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
