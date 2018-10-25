n=int(input("Enter Max:"))
d=int(input("Enter number:"))
for i in range(1,n+1,1):
    if(i%d==0):
        print(i,end=" ")
