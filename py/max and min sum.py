l=[]
m1=0
m2=0
n=int(input("Enter no.of elements:"))
for i in range (n):
    l.append(int(input()))
l.sort()
for i in range(4):
    m1=m1+l[i]
l.sort(reverse=True)
for i in range(4):
    m2=m2+l[i]
print("Max=",m2,"Min=",m1)
