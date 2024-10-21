'''
x=input()

y=x.split()

for var in y:
    print(var)
'''
'''
l=[10,11,12,13,14,15]

for i in l:
    #if l.index(i)%2==0:
        l.remove(i)
        print(l)
    
        
'''
'''
s="1 2 3 4 5 6 7 8 "
s1=s.replace(" ","")
for i in range(0,len(s1)):
    if int(s1[i])%2==0:
        print(s1[i])

for i in s:
    print(ord(i))
'''
'''
d={1:2,3:4,5:6,7:8}
for n in d:
    print (n,d[n])
'''
print('Give me any year.')
x=int(input())
if x%4==0 and x%100!=0 or x%400==0:
    print(x, 'is a leap year!')
else:
    print(x, 'is not a leap year!')
