#Create a list of 5 value with filename and extension. Replace extension with".c" with ".py" and print new list.
filenames=["program.c","stdio.c","sample.c","a.py","math.py","hpp.py"]
for i in range(len(filenames)):
    if filenames[i].endswith(".c"):
        filenames[i]=filenames[i][:-1]+"py"
print("\n",filenames)    
