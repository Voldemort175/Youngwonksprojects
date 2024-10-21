import time
i=1
j=1
while True:
   if i<=10:
       print(i)
       time.sleep(0.1)
       i+=j
   if i==10:
       j=-1
   if i==1:
       j=1
