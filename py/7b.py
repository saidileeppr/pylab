l=[]
t=0
n=int(input("Enter no.of elements:"))
print("Enter elements")
for i in range(n):
    l.append(int(input()))
ch=int(input("1.Ascending order  2.Descending order\n"))
if(ch==1):
    for i in range(0,n):
        for j in range(0,n-1):
            if(l[j]>l[j+1]):
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
    print(l)
elif(ch==2):
    for i in range(0,n):
        for j in range(0,n-1):
            if(l[j]<l[j+1]):
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
    print(l)
else:
    print("Select correct option ")
