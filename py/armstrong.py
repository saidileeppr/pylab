n=int(input("Enter number:"))
s=0
m=n
while(n!=0):
    i=n%10
    s=s+(i*i*i)
    n=n//10
if(s==m):
    print("Given number is an armstrong number")
else:
    print("Given number is not an armstrong number")
