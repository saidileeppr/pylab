st=input("Enter string:")
l=list(st)
c=0
w=1
for i in l:
    c=c+1
    if(i==' '):
        w=w+1
print(c,w)
