n=int(input("Enter number:"))
m=n
s=0
while(n!=0):
    b=n%10
    i=1
    while(b!=0):
        i=i*b
        b=b-1
    s=s+i
    n=n//10
if(s==m):
    print("Given number is a strong number")
else:
    print("Given number is not a strong number")
        
