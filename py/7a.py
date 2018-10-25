l=[]
f=0
n=int(input("Enter no.of elements:"))
print("Enter elements")
for i in range(n):
    l.append(int(input()))
print("Enter Key element:")
k=int(input())
for i in range(n):
    if(k==l[i]):
        f=1
        print("Element found at index",i)
if(f==0):
    print("Element not found")
