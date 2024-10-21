'''
import random

sum =0

f=open("random1000.txt","w")
for i in range(0,5):
    rand=random.randint(1,10)
    f.write(str(rand))
f.close()

f=open("random1000.txt","r")
j=f.read()
for i in j:
    sum=sum+int(i)
print("sum =", sum)
'''
'''
import time
print("source file")
s=input()
print("dest file")
d=input()

l=[]
f=open(s,"r")

for i in f:
    print(i)
    x,y=i.split(" ")
    j=x[0]+y[0:-1]
    l.append(j)
f.close()  
g=open(d,"w")
for i in l:
    g.write(i)
    g.write("\n")
g.close()
'''
'''
def count():
    cnt=0
    f=open("words.txt","r")
    for i in f:
        cnt+=1
    if cnt==0:
        print("no words found")
    print(cnt)
    return cnt
           
count()
'''

s="abcdefghijklmnopqrstuvwxyz"
d={}
c=0
f=open("words.txt","r")
##for j in f:
##    if j[0] not in d:
##        d[j[0]]=1
##    else:
##        d[j[0]]+=1
for i in f:
    if i[0] not in d:
        c=0
    for j in s:
        if i[0]==j:
            c+=1
            d[j]=c
    
    
print(d)
f.close()
'''
'''
'''
f=open("words.txt","r")
a=input()
b=input()
c=input()

for i in f:
    if a in i and b in i and c in i:
        print(i)

f.close()
'''
'''
cnt=0
f=open("words.txt","r")
j=f.read()
for i in range(0,len(j)):
    if j[i]=="\n" and j[i-1]=="y":
        cnt+=1
print(cnt)
'''
'''
f=open("words.txt","r")
for i in f:
  x=i
  if x==x[::-1]:
      print(x)
f.close()
    
'''

'''

f=open("words.txt","r")
for line in f:
    line = line.strip() # remove leading/trailing whitespace
    if line==line[::-1]:
        print(line, "is a palindrome")

'''
'''
questions = []
answers = []

# read questions from file
file=open("questions.txt", "r") 
for line in file:
    questions.append(line)

# read answers from file
g=open("answers.txt", "r") 
for line in g:
    answers.append(line)

# get user name
name = input("What is your name? ")

# create an empty list to store user's answers
user_answers = []

# iterate through questions and check answers
score = 0
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Answer: ")
    user_answers.append(user_answer)
    if user_answer.strip() == answers[i].strip():
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

# print user answers and correct answers
print("User Answers:")
for i in range(len(user_answers)):
    print(user_answers[i], end=" ")
    print("Correct Answer:", answers[i])

# print score
print("Score:", score)

# save the user answers to a file
with open(name + "_answers.txt", "w") as file:
    for user_answer in user_answers:
        file.write(user_answer + "\n")
'''
'''
# open the file
with open("example.txt", "r") as file:
    # read the contents of the file
    content = file.read()

# replace all spaces with '_'
content = content.replace(" ", "_")

# open the file for writing
with open("example.txt", "w") as file:
    # write the modified content to the file
    file.write(content)

print("All spaces in the file have been replaced with '_'.")
'''


with open("example.txt", "r") as file:
    # read the contents of the file
    content = file.read()

# replace all spaces with '_'
content = content.replace(" ", "_")

# open the file for writing
with open("example.txt", "w") as file:
    # write the modified content to the file
    file.write(content)
