n=int(input("Enter number:"))
a=n*n
b=a
su=0
count=0
while(a!=0):
    a=a//10
    count=count+1
d=count//2
while(b!=0):
    s=b%(pow(10,count-d))
    su=su+s
    b=b//(pow(10,count-d))
if(su==n):
    print("Given number is a karprekar number")
else:
    print("Given number is not a karprekar number")
