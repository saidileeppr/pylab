l=[]
m=int(input("Enter no.of elements:"))
for i in range (m):
    l.append(int(input()))
n=len(l)
i1=[]
for i in range(n):
    for j in range(n):
        if(i>j and l[i]==l[j]):
            print(l[i],"appeared at ",i,j)
            i1.append(i)
            i1.append(j)
e=int(input("Which element  do u want to delete:"))
s=int(input("Which index occurence do u want to delete:"))
del l[s]
print(l)
