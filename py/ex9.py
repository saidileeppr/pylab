s=input("Enter string:")
l=list(s)
l1=[]
for i in range(len(l)-1,-1,-1):
    l1.append(l[i])
if(l1==l):
    print("is palindrome")
else:
    print("not palindrome")
