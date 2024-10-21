'''
dict={"bob":98187, "ryan":67866, "mike":12987, "walter":45637}
print(dict["ryan"])
print(dict.keys())
print(dict.values())
for i in dict:
    print(i,dict[i])    
dict["white"]=674564
print(dict)
dict.pop("white")
'''
#product price
'''
dict={"laptop":1000,"phone":500,"lamp":30,"mouse":50,"bottle":10}
print("The products available are:",dict.keys())
print("which item do you want to buy?")
buy=input()
if(buy in dict):
    print("price=",dict[buy])
else:
    print("try elsewhere")
'''

#Admin
'''
login={"dad":1234,"mom":9876,"sis":4567,"me":3456}
print("enter your name")
name=input()
if name in login:
    print("Enter password")
    pwd=int(input())
    if (pwd == login[name]):
        print("Succesful login")
    else:
        print("Wrong password")
else:
    print("No Account found")
'''
#quiz game
'''
import random
s=0
quiz={" How many days do we have in a week?":"7"," How many days are there in a normal year?":"365","How many colors are there in a rainbow?":"7","How many letters are there in the English alphabet?":"26"," How many sides are there in a triangle?":"3","Which month of the year has the least number of days?":"February","Which animal is called King of Jungle?":"Lion","Which is the tallest animal on the earth?":"Giraffe"}
for i in range(0,10):
    q=random.choice(list(quiz))
    print(q)
    ans=input()
    if (ans == quiz[q]):
        s+=1
        print("Correct answer")
    else:
        print("Wrong answer")
        print(" correct answer is ", quiz[q])
        
print("total score is",s)        
'''
#tic tac toe
dict={
    "1":"","2":"","3":"",
    "4":"","5":"","6":"",
    "7":"","8":"","9":""
    }
turn = "x"
check = 0
while True:
    for w in dict:
        print(w,":",dict[w],"",end="")
        if (int(w) % 3) == 0:
            print("")
    print("Enter the number")
    inp=input()
    if turn =="x":
        dict[inp] = "x"
        turn = "o"
    else:
        dict[inp] = "o"
        turn = "x"
    if dict["1"] == dict["2"] == dict["3"] !="":
        check=1
    elif dict["4"] == dict["5"] == dict["6"] !="":
        check = 1
    elif dict["7"] == dict["8"] == dict["9"] !="":
        check = 1
    elif dict["4"] == dict["5"] == dict["6"] !="":
        check = 1
    elif dict["1"] == dict["4"] == dict["7"] !="":
        check = 1
    elif dict["2"] == dict["5"] == dict["8"] !="":
        check = 1
    elif dict["3"] == dict["6"] == dict["9"] !="":
        check = 1
    elif dict["1"] == dict["5"] == dict["9"] !="":
        check = 1
    elif dict["3"] == dict["5"] == dict["7"] !="":
        check = 1
    if check==1:
        if turn =="x":
            turn="o"
        else: turn="x"
        print("Player",turn,"has won")
        
        break
