l=[1,2,3,4,5,6,7,8,9,36,74]
s=0
a=0
for i in l:
    if(i>s):
        s=i
for i in l:
    if(i>a and i!=s):
        a=i
print(a)
