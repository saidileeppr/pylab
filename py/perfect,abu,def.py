n=int(input("Enter Range:"))
s=0;
print("1  is a perfect number")
for j in range(2,n+1):
    s=0
    for i in range(1,j):
        if(j%i==0):
            s=s+i
    if(j==s):
        print(j," is a perfect number")
    elif(j>s):
        print(j," is a deficient number")
    else:
        print(j," is a abundant number")

