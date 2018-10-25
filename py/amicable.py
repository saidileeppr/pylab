a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
i=1
s1=0
s2=0
while(i<=a):
    if(a%i==0):
        s1=s1+i
    i=i+1
i=1
while(i<=b):
    if(b%i==0):
        s2=s2+i
    i=i+1
if(s1==s2):
    print("Given number is a amicable number")
else:
    print("Given number is not a amicable number")
