'''
j=1
i=1
while i<=50:
   print(i)
   i+=j
   if i==50:
       j=-1
   if i==0:
       break
'''
'''
x = 0
a = 50
while True:
  if x < 50:
    x = x + 1
    print(x)
  if x == 50:
    a = a - 1
    print(a)
  if a == 0:
    break
'''
'''
n = 3
step = 1
count = 1

for i in range(1,30,n+1): 
   print(count,end= " ")
   count += step
   step += 1
'''
for count in range(1,11,1):
    print(count*count)
    
