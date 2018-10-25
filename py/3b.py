#AIM:TO WRITE AND READ CONTENT IN A FILE
a=input("enter file name:")
f=open(a,'a+')
print("Enter file content:")
s=''
while(s!='$'):
    f.write(s+'\n')
    s=input()
f.seek(0,0)
print("File content:")
s1=f.read()
print(s1)
f.close()
"""INPUT/OUTPUT:
enter file name:dfjskf
Enter file content:
sjfksfh
sfbsfjk
hfksjehf
$
File content:

sjfksfh
sfbsfjk
hfksjehf
"""
