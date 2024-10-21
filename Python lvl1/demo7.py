##for l in range(3):
##    for i in range(1,7,1):
##        for j in range(0,6-i,1):
##            print(" ",end="")
##
##        for k in range(1,2*i):
##            print("X", end="")
##        
##        print()
##for i in range(1,10,1):
##    for j in range(0,5):
##        print(" ",end="")
##
##    print("X")

#count from -17 to 25 and then back to 8
##rows = 5
##
##for i in range(1, rows+1):
##    # nested loop to print spaces
##    for j in range(rows-i):
##        print(" ", end="")
##    # nested loop to print asterisks
##    for k in range(i):
##        print("* ", end="")
##    # move to the next line
##    print()


rows = 4

for i in range(rows):
    # print spaces before asterisks
    for j in range(i):
        print("  ", end="")
    # print asterisks
    for k in range(rows-i):
        print("*  ", end="")
    # move to the next line
    print()
