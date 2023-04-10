#Write a script to Replace list’s item with new value if found. Take value from user which you want to replace.
def replace(r,rw,list1):
    for i in range(len(list1)):
        if list1[i]==r:
            list1[i]=rw
    return(list1)
l=[]
n=int(input("How many number you want to enter:"))
for i in range(n):
    s=int(input("Enter a number:"))
    l.append(s)
r=int(input("Enter value you want to replace:"))
rw=int(input("nter value you want to replace with:"))

l=replace(r,rw,l)
print("\n",l)
