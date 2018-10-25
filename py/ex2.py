st=input("Enter string:")
c=0
l=list(st)
t=l[0]
l[0]=l[len(l)-1]
l[len(l)-1]=t
s=''.join(l)
print(s)
