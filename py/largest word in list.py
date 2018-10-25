l=[]
n=int(input("Enter no.of words"))
for i in range(n):
    l.append(input())
m=0
for i in l:
    if(len(i)>m):
        m=len(i)
        h=i
print(h)
