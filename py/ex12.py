s=input("enter string:")
l=s.split(" ")
print(l)
for i in l:
    k=i
    c=l.count(i)
    print(i,":",c)
    if(c>1):
        for j in l:
            while(c>1):
                 if(i==j):
                     l.remove(k)
                     c=c-1
                 
       
