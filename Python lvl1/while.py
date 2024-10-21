#count
'''
i=20
while i>=0:
    print(i)
    i-=1
i=0
while i<35:
    i+=1
    print(i)
'''
#17 to 25 then to 8
'''
i=-17
while i<=25:
    print(i)
    i+=1
while i>=8:
    print(i)
    i-=1
print("Bing")
'''
#countdown timer
'''
import time

print("How many seconds?")
i = int(input())
while i>=1:
    print(i)
    time.sleep(1)
    i-=1
print("BLAST OFF")
'''
#enter quit
'''
i="hi"
while not(i=="quit"):
    print("Enter a word")
    i=input()
'''
#guess
'''
import random
var = random.randint(1,10)
i=-1
cnt=1
while not(i==var):
    print("Enter your guess")
    i=int(input())
    cnt+=1
    if cnt>3:
        print("too many wrong attempts")
        break
'''

'''
while True:
    print("enter string")
    s=input()
    for i in s:
        print(i)
 '''

import random
var=random.randint(20,30)
choice =0
chances=0
while (var!=choice):
    print("ENter guess between 20 and 30")
    choice=int(input())
    chances+=1
print("you took",chances,"chances to get it right")   
