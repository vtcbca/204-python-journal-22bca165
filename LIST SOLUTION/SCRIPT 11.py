#Write a Python program to enter sentence of atleast 10 words. Take user input of lengtho of word. 
#Find the word in user inputed string which has >= length of word enter by user and creaet its directory where word is key and its length is value.
s=input("Enter string:")
n=int(input("Minimum word length:"))
dic={}
l=s.split()
for i in l:
    if len(i)>=n:
        dic[i]=[len(i)]

print(dic)
        
