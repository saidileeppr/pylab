s=input("Enter string")
l=list(s)
c=0
for i in l:
    if(ord(i)>=ord('a') and ord(i)<=ord('z')):
        c=c+1
print(c)
