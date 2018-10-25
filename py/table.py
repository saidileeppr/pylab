ch=int(input("1.All 2.Single"))
a="http://202.53.67.26/examsportal/verify/photos/bt"
b=str(input("Enter year:"))
c=int(input("Enter branch code:"))
l=[]
if(c<10):
    c='0'+str(c)
a=a+b+'/'+str(c)+'/'
def all():
    for i in range(48,58):
        for j in range(48,58):
            l.append('wget '+a+b+'121A'+str(c)+chr(i)+chr(j)+'.jpg')
    for i in range(65,85):
        for j in range(48,58):
            l.append('wget '+a+b+'121A'+str(c)+chr(i)+chr(j)+'.jpg')
def one():
    l.append('wget '+a+b+'121A'+c+f+'.jpg')
if(ch==1):
    all()
if (ch==2):
    one()
import os
for i in l:
    os.system(i)
