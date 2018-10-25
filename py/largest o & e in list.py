l=[1,3,4,2,5,7,6,8,63,20]
e=0
odd=0
for j in l:
    if(j%2==0 and j>e):
        e=j
    if(j%2!=0 and j>odd):
        odd=j
print("largest even=",e,"largest odd=",odd)
