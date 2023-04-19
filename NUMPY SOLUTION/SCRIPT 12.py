import numpy as np

l=[]
ch='y'
while ch=='Y' or ch=='y':
    s=float(input("Enter a number:"))
    l.append(s)
    ch=input("Do you want to enter more number? (Yes=y/Y,No=N/n):")

a=np.array(l)

print("\n",l)
print("\n",a)
