l=[]
c=-1
n=int(input("Enter no.of elements:"))
for i in range(n):
    l.append(int(input()))
for i in l:
    b=l.count(i)
    if(b>1):
        while(b>1):
            l.remove(i)
            b=b-1
        
c=l
print(c)
