s=input("Enter any sentense:")
l=list(s.split(" "))
c=0
a=[]
for i in l:
    r=i[::-1]
    if r==i:
        print(i)
        c=c+1
        a.append(i)
        
        
print("total {} palindrom word in string:".format(c))
