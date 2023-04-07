def evench(l):
    c=0
    n=[]
    for i in l:
        if len(i)%2==0:
            c=c+1
            n.append(i)
    if c>0:
        print(n)
    else:
        print("There is no Name having the length of even numbers")
     
def replace(l):
    for i in l:
        for j in range(len(i)):
            if j%2==0:
                print(i[j],end="")
            else:
                print(j,end="")
        print("\n")
                
def extract(l):
    s=input("Enter starting value:")
    e=input("Enter ending value:")
    f=0
    for i in l:
        if(i[0]==s and i[-1]==e):
            print(i)
            f=1
    if(f==0):
        print("NO data found.")
            

l=[]
c=0
ch="y"
a="y"

while ch=='Y' or ch=='y':
    s=input("Enter a string:")
    l.append(s)
    ch=input("\nDo you want to enter more string? (Yes=y/Y,No=N/n):")
    
while(a=='Y' or a=='y'):
    print("\n\n1.Print string with even character in length.")
    print("2. Replace odd character of string with index no.")
    print("3.Enter start and end value and extract character from the list of string.")
    print("-------------------------------------------------------------------------------")
    c=int(input("Enter your choice:"))
    if(c==1):
          evench(l)
    elif(c==2):
          replace(l)
    elif(c==3):
        extract(l)
    else:
        print("\nEnter a valid choice.")
    ch=input("Do you want to continue:")


            
        
        
        
