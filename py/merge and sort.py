m=[1,2,3,4]
l=[5,6,7,8,9]
t=0
for i in m:
    l.append(i)
for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if(l[j]>l[j+1]):
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
print(l)
