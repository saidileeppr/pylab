l=[]
s1=0
s2=0
c1=0
c2=0
c3=0
a=int(input("enter range:"))
print("enter positive or negative or zeroes:")
for i in range(a):
    l.append(int(input()))
for i in l:
    if(i>0):
        c1=c1+1
        s1=s1+i
    elif(i<0):
        c2=c2+1
        s2=s2+i
    else:
        c3=c3+1
print("avg of positive is:",s1/c1)
print("avg of negative is:",s2/c2)
print("the no.of 0's are:",c3)


