'''
d={"Maths":5, "history":8, "science":3,"sst":6,"comp":9,"art":11}
##print(d)
x=list(d.keys())
##print(x)
y=sorted(d.values())

print(x)
print(y)
##print(y)
##print(type(y))

##    sublist=list(d.keys())
##             print(sublist[y])
for i in range(0,len(x)):
    position=y.index(x[i])
    print(x[position])
'''
#Question 3
#Question 4
'''
S='this is a sentence'
for i in range(0,len(S),1):
    if i%2==0:
        print(S[i].upper(),end="")
    else:
        print(S[i],end=""s)
'''


superheroes = ["Flash", "Hulk", "Superman", "Spiderman", "Ironman"]

for x in superheroes:
  string = list(x)
  string.reverse()
  print("".join(string),end = "")

'''
def countVowels(string):
    num_vowels = 0
    for value in string:
        if value in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels

string = input('Enter any string: ')
print("Number of vowels is: ",countVowels(string))
'''

'''
import random

def pair():
  monuments = ("Notre Dame", "Nigeria Falls", "Buckingham Palace", "London Eye")
  Adjectives= ("beautiful", "marvelous", "amazing" , "magnificent")
  pair =  [(a, b) for a in monuments for b in Adjectives]
  x,y = random.choice(pair)
  print(str(x) + " is " + str(y))
  
pair()
'''
'''
myDict = {"dogs":"","cats": "","elephants": "", "ducks": "", "lions": ""}
print("Dictionary Before = ", myDict)

for x in myDict:
    a = input("What sound do " + str(x) + " make?")
    myDict[x] = a
    
print("Dictionary After = ", myDict)
'''
'''
string = input("Enter a word: ")
a = {}

for value,letter in enumerate(string): 
    a[letter] = value

print(a)
'''
'''
pin=[4,5,6,7]

for i in range(len(pin)-1,-1,-1):
    print(pin[i])
'''
'''
print('what is your name')
name=input()
user=name
print('hello,',user)
'''
'''
ht_cm=int(input('how tall are you in centimeters:'))
print('Your height in feet :',(ht_cm)/30.48)
'''

#Question 2
#Question 3
#Question 4
'''
import random
a=[]
c=0
q=0
for b in range(0,7,1):
    while True:
        q=0
        c=str(random.randint(10000,99999))
        for d in a:
            if c==d:
              q=1
        if q==0:
            a.append(c)
            break
print("This is the list of numbers that we'll be working on:")
for b in range(0,len(a),1):
    print(a[b],end=" ")
    if b==6:
        print("")
z=[]
for b in a:
    d=0
    for q in range(0,5,1):
        d=d+int(b[q])
    z.append(d)
q=max(z)
w=[]
for b in range(0,len(z),1):
    if q==z[b]:
        w.append(a[b])
if len(w)==1:
    print("The number who's sum of digits is the greatest is", end=" ")
elif len(w)==2:
    print("The numbers whose sum of digits both are the greatest are", end=" ")
else:
    print("The numbers whose sum of digits all are the greatest are", end=" ")
for q in range(0,len(w),1):
    print(w[q], end="")
    if len(w)==1:
        print(".")
    elif len(w)==2:
        if q==0:
            print(" and", end=" ")
        else:
            print(".")
    else:
        if q==len(w)-2:
            print(", and", end=" ")
        elif q==len(w)-1:
            print(".")
        else:
            print(",", end=" ")
'''
'''
prod=1
for i in range(2,5):
    prod=i*prod

print(prod)
'''
'''
num={}
l=[]
x=1

while x<101:
    num[x]=x*x
    if x%10==0:
        l.append(x)
    x+=1   
      
print(num)

for i in l:
    del num[i]
        
    
print(num)
'''
'''
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
position = [300, 300]
direction = 'RIGHT'
change_to = direction

while True:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255),position,30)
    if position[0] >= 600:
        position[0] = 30
    if position[0] <= 0:
        position[0] = 600
    if position[1] >= 600:
        position[1] = 30
    if position[1] <= 0:
        position[1] = 600
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.type == QUIT:
                pygame.quit()
                exit()
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        
    if direction == 'UP':
        position[1] -= 10
    if direction == 'DOWN':
        position[1] += 10
    if direction == 'LEFT':
        position[0] -= 10
    if direction == 'RIGHT':
        position[0] += 10

    pygame.display.update()
'''
