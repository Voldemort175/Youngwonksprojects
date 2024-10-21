#Question 2
print("bir(year1,month1,day1,year2,month2,day2)")
def fin(a,b):
    if a>b:
        final=a-b
    else:
        final=b-a
    day=final.days
    print("They are",day,end=" ")
    if day==1:
        print("day apart.")
    else:
        print("days apart")
def bir(a1,a2,a3,b1,b2,b3):
    import datetime
    a=datetime.datetime(a1,a2,a3)
    b=datetime.datetime(b1,b2,b3)
    fin(a,b)
