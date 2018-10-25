#AIM:TO FIND SUM OF INDIVIDUAL DIGITS OF A NUMBER
n=int(input("enter number:"))
s=0
while(n>0):
    s=s+n%10
    n=n//10
print("sum=",s)
"""
INPUT/OUTPUT:
enter number:1234
sum= 10
"""
