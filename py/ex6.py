s=input("Enter string:")
l=list(s)
c=0
l1=[]
print(len(l))
for i in l:
    if(c%2==0):
        l1.append(i)
    c+=1      
print(l1)
