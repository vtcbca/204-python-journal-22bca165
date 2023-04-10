#Write a script to create dictionary from list which contain student id , name and percentage
#Take student id and name till user choise.
ch="Y"
List=[]
Dict={}
while ch=='Y' or ch=='y':
    sid=int(input("\nstudent id:"))
    List.append(sid)
    sname=input("student name:")
    List.append(sname)
    sper=float(input("student percentage:"))
    List.append(sper)
    ch=input("\nDo you want to enter detail for more student? (yes=Y/y,No=N/n):")

for i in range(0,len(List),3):
    Dict[List[i]]=[List[i+1],List[i+2]]

print("List",List)
print("Dictionary:",Dict)

    
    
