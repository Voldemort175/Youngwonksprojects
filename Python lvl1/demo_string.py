s="aeiou"

inp = input()
li=list(inp)
for i in range(0,len(li)):
    if i%2==0 and li[i] in s:
        li[i]="-"

print("".join(li))


        

