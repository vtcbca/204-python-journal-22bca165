s=input("Enter any string:")

half=int(len(s)/2)

fs=s[:half]
ss=s[half:]

if fs==ss:
    print("String is Symmetrical.")
else:
    print("String is not Symmetrical.")
