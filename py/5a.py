#AIM:TO DISPLAY FIBONACCI SERIES USING WHILE AND FOR LOOPS
n=int(input("Enter range:"))
a=0
b=1
print("For loop:")
for i in range(1,n+1,1):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
print("\nWhile loop:")  
a=0
b=1
i=1
while(i<=n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i=i+1
    
"""INPUT/OUTPUT:
Enter range:9
For loop:
0 1 1 2 3 5 8 13 21 
While loop:
0 1 1 2 3 5 8 13 21"""
