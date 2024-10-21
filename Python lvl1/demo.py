'''
u=0
l=["Ironman","The vison","doctor strange","superman","thor"]
for n in range(0,5,1):
    v=list(l[u])
    v.reverse()
    "".join(v)
    print("".join(v),end="")
    u=u+1
'''
#Question 2
#Question 3
#Question 4
'''
a=[]
b=1
d=[]
w=0
q="1"
print("Let's make a 10 number list.")
while b<11:
    w=0
    print("Enter the ", end=str(b))
    if q[-1]=="1":
        print("st", end=" ")
    elif q[-1]=="2":
        print("nd", end=" ")
    elif q[-1]=="3":
        print("rd", end=" ")
    else:
        print("th", end=" ")
    print("number on the list.")
    c=input()
    for y in c:
        if y==".":
            w=w+1
    if w<2:
        a.append(c)
        b=b+1
        q=str(b)
    else:
        print("THIS IS NOT A NUMBER!")
c=0
for b in a:
    w=0
    if not "." in b:
        if not b[-1]=="4":
            d.append(b)
            c=1
    else:
        for z in range(0,len(b),1):
            if b[z]==".":
                w=z
        if not b[z-2]=="4":
            d.append(b)
            c=1
if c==0:
    print("Here's the list:")
else:
    print("Here's the list, edited by yours truly, since I don't like numbers that have 4 in their units place:")
print(d)
'''


