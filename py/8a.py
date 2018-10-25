#AIM:TO FIND GCD OF 2 NUMBERS USING RECURSION
def fun(x,y):
    if(x%y==0):
        return y
    else:
        return fun(y,x%y)
n=int(input("Enter:"))
m=int(input("Enter:"))
print("Result=",fun(n,m))
"""
INPUT/OUTPUT:
Enter:18
Enter:16
Result= 2
"""
