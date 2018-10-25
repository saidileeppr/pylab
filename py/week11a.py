import sys
try:
    number = int(input("Enter a number"))
    print(a)
except ValueError:
    print("enter numbers only")
    sys.exit(1)
except NameError:
    print("assign value to 'a' then try to use")
print("you entered number ", number)
"""INPUT/OUPUT:
Enter a number45
assign value to 'a' then try to use
you entered number  45"""
