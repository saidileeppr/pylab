n=int(input("Enter number:"))
i=0
print("Even numbers:")
while(i<=n):
    if(i%2==0):
        print(i,end=',')
    i=i+1
i=0
print("\nOdd numbers:")
while(i<=n):
    if(i%2!=0):
        print(i,end=',')
    i=i+1
