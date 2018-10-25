#AIM:TO DISPLAY THREE NUMBERS IN ASCENDING ORDER
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
print("ASCENDING ORDER")
if(a>b and a>c):
    if(b>c):
        print(c,b,a)
    else:
        print(b,c,a)
    print("largest number:",a)
if(b>c and b>a):
    if(a>c):
        print(c,a,b)
    else:
        print(a,c,b)
    print("largest number:",b)
if(c>a and c>b):
    if(a>b):
        print(b,a,c)
    else:
        print(a,b,c)
    print("largest number:",c)
else:
    print("All are equal")

"""
INPUT/OUTPUT:
enter first number:56
enter second number:89
enter third number:32
ASCENDING ORDER
32 56 89
"""

 
