p=int(input("Enter Principal:"))
r=int(input("Enter rate of interest:"))
t=float(input("Enter no.of years:"))
i=(p*t*r)/100
emi=(p+i)/(t*12)
print("EMI=",emi)
