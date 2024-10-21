#age above 16
'''
print("Enter age")
age=int(input())
if age>=16:
    print("Eligible to drive")
else:
    print("Sorry you cant drive yet. You have to wait",16-age,"more years")
'''
#even or odd
'''
print("Enter a number")
num=int(input())
if (num % 2 == 0):
    print("even")
else:
    print("odd")
'''

#grade
'''
print("Enter the score")
s=int(input())
if (90<=s<=100):
    print("Grade A")
elif (80<=s<=89):
    print("Grade B")
elif (70<=s<=79):
    print("Grade C")
elif (60<=s<=69):
    print("Grade D")
elif (0<=s<=59):
    print("Grade F")
else:
    print("Invalid score")
'''

#discount calc
'''
print("Enter purchase price")
p=int(input())
if (p > 10):
    print("20% discount")
    print("\n Final price=",80*p/100)
elif (0<p<=10):
    print("10% discount")
    print("\n Final price=",90*p/100)
else:
    print("Enter valid amount")
'''

#age and grade
'''
print("Enter age")
age=int(input())
print("Enter grade")
grade=int(input())
if (age>=8,grade>=3):
    print("Eligible to play")
else:
    print("not eligible")
 '''
#state check
'''
print("Enter you state")
state=input()
if ((state=="California") or (state=="Oregon") or (state=="Washington")):
    print("We suggest you go for a coastal drive")
else:
    print("You may be better of skiing")
'''
#vacation check
print("Do you have an upcoming vacation?")
ans=input()
if (ans == "yes"):
    print("What grade are you in?")
    grade=int(input())
    if(grade == 12):
        print("great time to study for SAT")
    else:
        print("Have an adventurous vacation")
 
 
    
