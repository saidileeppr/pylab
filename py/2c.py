#AIM:TO DISPLAY PRIME NUMBERS UPTO A GIVEN RANGE
n=int(input("enter input:"))
i=2
d=1
while(i<=n):
        j=1
        count=0
        while(i>j):
            if(i%j==0):
                count=count+1
            j=j+1
        if(count==1):
            print(j)
        i=i+1
"""
INPUT/OUTPUT:
enter input:17
2
3
5
7
11
13
17
"""
