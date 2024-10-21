'''a1 = {'a':1, 'b':13, 'd':4, 'c':2, 'e':30}
a1_sorted_keys = sorted(a1, key=a1.get, reverse=True)
for r in a1_sorted_keys:
    print(r, a1[r])
'''
'''
#Question 1
a={"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}
c=0
letter="X"
winner=""
while True:
    for b in a:
        c=c+1
        print(b+":"+a[b],end="      ")#8 spaces
        if c==3:
            print("")
            c=0
    if not winner=="":
        break
    print("Select the placement for:",letter)
    choice=input()
    if choice in a:
        if a[choice]==" ":
            a[choice]=letter
            if letter=="X":
                letter="O"
            else:
                letter="X"
        else:
            print("Please re-enter the placement.")
    
    elif choice=="END":
        break
    else:
        print("Please re-enter the placement.")
    #Horizantal
    list1=[]
    list2=[]
    list3=[]
    count=0
    for w in a:
        count=count+1
        if str(count)=="1" or str(count)=="2" or str(count)=="3":
            list1.append(a[w])
        elif str(count)=="4" or str(count)=="5" or str(count)=="6":
            list2.append(a[w])
        else:
            list3.append(a[w])
    lists=[list1,list2,list3]
    for w in range(0,3,1): 
        if not "X" in lists[w] and not " " in lists[w]:
            winner="O"
            break
        elif not "O" in lists[w] and not " " in lists[w]:
            winner="X"
            break
    #Vertical
    list1=[]
    list2=[]
    list3=[]
    count=0
    for w in a:
        count=count+1
        if str(count)=="1" or str(count)=="4" or str(count)=="7":
            list1.append(a[w])
        elif str(count)=="2" or str(count)=="5" or str(count)=="8":
            list2.append(a[w])
        else:
            list3.append(a[w])
    lists=[list1,list2,list3]
    for w in range(0,3,1): 
        if not "X" in lists[w] and not " " in lists[w]:
            winner="O"
            break
        elif not "O" in lists[w] and not " " in lists[w]:
            winner="X"
            break
    #Across
    list1=[]
    list2=[]
    count=0
    for w in a:
        count=count+1
        if str(count)=="1" or str(count)=="9":
            list1.append(a[w])
        elif str(count)=="3" or str(count)=="7":
            list2.append(a[w])
    list1.append(a["5"])
    list2.append(a["5"])
    lists=[list1,list2]
    for w in range(0,2,1): 
        if not "X" in lists[w] and not " " in lists[w]:
            winner="O"
            break
        elif not "O" in lists[w] and not " " in lists[w]:
            winner="X"
            break
print(winner,"won!")
'''

