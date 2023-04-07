def leneven(l):
    c=0
    n=[]
    for i in l:
        a=len(i)
        if a%2==0:
            c=c+1
            n.append(i)
    print("Total string of even number of character:{}".format(c))
    for j in n:
        print(j)

ch='Y'
l=[]
while ch=='Y' or ch=='y':
    n=input("Enter a name:")
    l.append(n)
    ch=input("\nDo you want to enter more name? (Yes=y/Y,No=N/n):")

leneven(l)
