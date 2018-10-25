f=open("asdfnhi",'a+')
s=input("ENter content:")
while(s!='$'):
    f.write(s+"\n")
    s=input()
f.seek(0,0)
s1=f.read()
c=input("Enter the character:")
n=s1.count(c)
s3=s1.replace(c,'')
f.close()
f1=open("ahgfcsd",'a+')
f1.write(s3)
f1.seek(0,0)
s2=f1.read()
print(s2)
print("No.of occurences:",n)
f1.close()
"""INPUT/OUTPUT:
ENter content:abcdabcdabcd
abcdabcd
abcd
$
Enter the character:a
bcdbcdbcd
bcdbcd
bcd

No.of occurences: 6"""
