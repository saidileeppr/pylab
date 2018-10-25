#AIM: TO CONVERT CELSIUS TO FARHENHEIT AND FARHENHEIT TO CELSIUS USING FUNCTIONS
def cf(x):
    return (x/5)*9+32
def fc(y):
    return (y-32)*5/9
ch=int(input("Which one do u want to enter 1.Celsius 2.Farhenheit :"))
n=int(input("Enter degrees:"))
if(ch==1):
    print("Degrees in Farhenheit=",cf(n))
elif(ch==2):
    print("Degrees in Celsius=",fc(n))
else:
    print("Enter correct option")
"""INPUT/OUTPUT:
Which one do u want to enter 1.Celsius 2.Farhenheit :1
Enter degrees:0
Degrees in Farhenheit= 32.0
"""
