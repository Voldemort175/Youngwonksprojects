'''
def header():
    print("This is a function")
    print("hello and bye")
    
'''
'''
def mean(n1,n2,n3,n4):
    return (n1+n2+n3+n4)/4
 '''
#reverse string func
'''
def rev(s):
    v=list(s)
    print(v)
    list.reverse(v)
    print(v)
    print("".join(v))
'''
#random name
'''
import random
def rname(s1,s2,s3,s4,s5):
    l=[s1,s2,s3,s4,s5]
    c=random.choice(l)
    print(c)
'''
#equation
'''
def eq(a,b,c):
    return a*(b*c)
'''
'''
#sort alphabets in ascending order
s ="GEEKSFORGEEKS"
 
li = []
l = len(s)
for i in range (0,l):
    li.append(s[i])
 
 
for i in range(0,l):
    for j in range(0,l):
        if li[i]<li[j]:
            li[i],li[j]=li[j],li[i]
j=""
 
for i in range(0,l):
    j = j+li[i]
 
print(j)
'''
#caeser cypher
'''
def encrypt_caesar(plain_text, rotation_factor):
    encrypted_text = ""
    a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small="abcdefghijklmnopqrstuvwxyz"
    caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in plain_text:
        if char in a:
            shift = ord(char) + rotation_factor
            if char in small:
                if shift > ord('z'):
                    shift = shift - 26
                encrypted_text += chr(shift)
            else:
                if shift > ord('Z'):
                    shift = shift - 26
                encrypted_text += chr(shift)
        else:
            encrypted_text += char
    return encrypted_text

plain_text = input("Enter a string to encrypt: ")
rotation_factor = int(input("Enter rotation factor: "))
encrypted_text = encrypt_caesar(plain_text, rotation_factor)
print("Encrypted text: " + encrypted_text)
