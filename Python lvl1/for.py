#name repeat
'''
for var in range(1,101):
    print("Ben", var)
'''

#odd or even
'''
for var in range(1,20):
    if (var % 2 == 0):
        print(var,"Even")
    else:
        print(var,"Odd")
'''
#countdown
'''
import time
print("How many seconds?")
s=int(input())
for var in range(s,0,-1):
    time.sleep(1)
    print(var)
print("BLAST OFF")
'''
#multiplication table
'''
print("Enter number")
num=int(input())
for i in range(1,11):
    print(num,"X",i,"=",num*i)
'''
#rectangle pattern
'''
for i in range(0,5):
    for j in range(0,5):
        print("*",end='')
    print("\n")
'''
#triangle pattern
'''
for i in range(0,4):
    for j in range(0,4):
        if (i>=j):
            print("*", end='')
    print("\n")
'''
# for step2
'''
for i in range(100,0,-3):
    if (20<i<30):
        print("Tick Tock")
    else:print(i)
'''

# big pattern
'''
print("Enter number of blocks")
b=int(input())
print("Enter block width")
w=int(input())
for k in range(0,b):
    for i in range(0,3):
        for j in range(0,w):
            print("*",end="")
        print("\n")
    print("\n\n\n")
'''
#random
'''
import random
import time

while True: 
    var = random.random()
    var2 = random.randint(-99999,99999)
    print(var,var2)
    time.sleep(3)
'''

#random mean
'''
import random
sum=0
for i in range(0,20):
    var=random.randint(-10000,10000)
    sum+=var
    print(var)
print("Average=",sum/20)
'''
#for with random
import random
sum=0
neg=0
for i in range(0,20):
    var=random.randint(-19,20)
    print(var)
    if (var>0):
       sum+=var
    else:
        neg+=var
    
print("Sum of positives=",sum)   
print("Average of negatives=",neg/20)
