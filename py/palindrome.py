n=int(input("Enter number:"))
m=0
t=n
while(n!=0):
    a=n%10
    n=n//10
    m=m*10+a
if(m==t):
    print("Given number is a palindrome")
else:
    print("Given number is not a palindrome")
        
