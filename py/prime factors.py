n=int(input("Enter Max:"))
d=int(input("Enter number:"))
for i in range(2,n+1,1):
    flag=0
    for j in range(2,i,1):
        if(i%j==0):
            flag=1
    if(d%i==0 and flag==0):
        print(i,end=" ")
    
