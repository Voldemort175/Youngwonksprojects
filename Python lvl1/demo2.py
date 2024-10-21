'''
groceries = { 'apples' : 11, 'eggs' : 6, 'milk' : 3, 'veggies' : 10, 'detergent' : 1 }
print(groceries)
groceries['snacks'] = 2
groceries['bread'] = 2
print(groceries)
'''
'''
s='Hello My Name Is'
print(s[-2])
for i in range(0,len(s),1):
    if s[i].isupper():
         print(s[i])
print(s[5:9])
for a in range(3,len(s),1):
    print(s[a], end = ' ')
print()
print(s.title())
'''
'''
print("ENTER RANDOM YEAR")
i=int(input())
if i%4==0:
  if i%100==0:
    if i%400==0:
      print("LEAP YEARRRRRR")
    else:
      print("NOT a leap year")
  else:
    print("NOT a leap year")
else:
  print("NOT a leap year")
'''
'''
a=int(input())
d={}
for i in range(1,11,1):
  d[i]=a**i
  
'''

for r in range(9,5,-1):

    print()
    for c in range (9,5,-1):
        
        if r>=c:
        
            print(r , end = "")























