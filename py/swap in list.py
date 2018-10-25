l=[1,2,3,4,5,6,7,8,9]
t=l[0]
l[0]=l[len(l)-1]
l[len(l)-1]=t
print(l)
