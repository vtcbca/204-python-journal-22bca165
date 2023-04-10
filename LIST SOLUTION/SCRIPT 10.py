#wriate a script to check if the list contains three consecutive common numbers in Python using udf.
def consecutivecoomon(l):
    count=0
    b=[]
    for i in range(len(n)-2):
        if n[i]==n[i+1] and n[i+1]==n[i+2]:
            b.append(n[i])
            count+=1
    if count>0:
        print(f"Consecutive common number in list {n} as follow:{b}")
    else:
        printf("No consecutive number in list")

n=[]
a=int(input("How many number you want to enter in list:"))
for i in range(a):
    c=int(input("Enter value:"))
    n.append(c)
consecutivecoomon(n)        

