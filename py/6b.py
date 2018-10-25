c1=int(input("Enter no.of columns:"))
r1=int(input("Enter no.of rows:"))
l=[]
l=[[int(input()) for j in range(c1)]for i in range(r1)]
m=[]
a=[]
p=[]
c2=int(input("Enter no.of columns:"))
r2=int(input("Enter no.of rows:"))
m=[[int(input()) for j in range(c2)]for i in range(r2)]
a=[[m[i][j]+l[i][j] for j in range(c2)]for i in range(r1)]
print("ADDITION:")
for i in range(r1):
    print(a[i])
p=[[0 for i in range(c2)] for j in range(r2)]
for i in range(r1):
    for j in range(c2):
        for k in range (c2):
            p[i][j]=(p[i][j]+l[i][k]*m[k][j])
print("MULTIPLICTION:")
for i in range(r1):
    print(p[i])
    
