n=int(input("Enter number:"))
c=0
i=n%10
while(n>0):
    n=n//10
    c=c+1
nn=(c*10)+i
print(nn)
