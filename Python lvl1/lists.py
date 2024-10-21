#lists
'''
friends=["onisan","okasan","neesan","obachan","senpai"]
print(len(friends))
print(friends[1])
print(friends[2:4])
friends[3]="tomodachi"
print(friends)
friends.insert(2,"friend")
print(friends)
friends.append("ichigo")
print(friends)
friends.pop(2)
print(friends)
friends.remove("okasan")
print(friends)
t=friends.pop(2)
print(t)
friends.sort()
print(friends)
f2=friends
f2.sort(reverse=True)
#friends.sort(reverse=False)
print(f2)
print(friends)
'''

#split and join
'''
var = "Hello how are you"
s=var.split()
print(s)
hello=list(var)
print(hello)
print("".join(hello))
'''

#password check
'''
l=[]
i="default"
cnt=1
while not(i=="pswd"):
    print("Enter password")
    i=input()
    if i!="pswd":
        l.append(i)
        cnt+=1
    if cnt>3:
        print("too many wrong attempts")
        break
if i=="pswd":
    print("Access Granted")
    print("Wrong passwords tried",l)
'''

#random list
'''
import random
l=[]
for i in range(0,20):
    r=random.randint(0,100)
    l.append(r)

print(l)
print("Max=",max(l),"min=",min(l))
'''
#random module
#shuffle
'''
import random
l=["Ben","kevin","gwen","max"]
for i in range(0,10):
    random.shuffle(l)
print(l[0])
print(random.choice(l))
print(random.sample(l,3))
'''

#string to list
'''
var="hello"
hi=list(var)
print(hi)
print("h" in hi)
'''
#string iteration
'''
a="hello how are you"
for var in range(len(a)):
    print(a[var])
l=["Ben","kevin","gwen","max"]
for i in l:
    print(i)
'''
#hangman game
'''
import random
l=["balloon"]
r=random.choice(l)
j=[]
p=list(r)
cnt=1
for i in range(0,len(r)):
    j.append("_")
for k in range(0,20):
    print(j)
    print("Enter a letter")
    letter=input()
    cnt+=1
    if letter =="ch":                  #cheat code
        for i in range(0,len(j)):
            if j[i]=="_":
                j[i]=p[i]
                break
    for i in range(0,len(p)):
        if letter==p[i]:
            j[i]=letter
            
            cnt-=1

    if j==p:
        print("you have won")
        print(j)
        break
    if cnt>10:
        print("too many wrong attempts")
        print(j)
        break

'''
#List of list

##ClassMark = [ 'Math', 'Writing','History','Science']
##BillMarks = [ 86 , 80 , 78 , 94 ] #List 1
##TomMarks = [ 65 , 78 , 79 , 87 ] #List 2
##Mikemarks = [ 89 , 76 , 87 , 75 ] #List 3
##
##twod=[BillMarks,TomMarks,Mikemarks]
##print(twod)
##print("Tom's history marks=",twod[2][2])
##print("Enter subject")
##sub=input()
##if sub in ClassMark:
##    index=ClassMark.index(sub)
##    print(index)
##   # print(twod[0][3])
##    avg=(twod[0][index] + twod[1][index] + twod[2][index])/3
##    #avg=(BillMarks[index] + TomMarks[index] + Mikemarks[index])/3
##    print("Average marks=",avg)
##

#Tuple
'''
t=("reba","ben","dad","mom")
print(t.index("reba"))
'''


#correct guess
'''
import random

l=[]
c=0
for i in range(0,10):
    l.append(random.randint(1,20))
print(l)
for i in range(0,7):
    j=int(input("Enter your guess from 1-20"))
    for k in range(0,len(l)):
        if l[k]==j:
            l[k]="Correct"
            c+=1
print("You got",c,"corect guesses")
print(l)
'''


l=["hi","my","name","is","nice"]
for i in range(0,len(l)):
               if i%2==0:
                   l.remove(l[i])
print(l)

