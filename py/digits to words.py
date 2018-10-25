n=int(input("Enter the number:"))
d=0
c=0
if(n==0):
    print("ZERO")
else:
    while(n>0):
        c=c+1
        d=(d*10)+n%10
        n=n//10
    while(d!=0):
        b=d%10
        if(c!=2 and c!=5 and c!=7 and c!=9):
            if(b==1):
                print("ONE",end=' ')
            if(b==2):
                print("TWO",end= ' ')
            if(b==3):
                print("THREE",end=' ')
            if(b==4):
                print("FOUR",end=' ')
            if(b==5):
                print("FIVE",end=' ')
            if(b==6):
                print("SIX",end=' ')
            if(b==7):
                print("SEVEN",end=' ')
            if(b==8):
                print("EIGHT",end=' ')
            if(b==9):
                print("NINE",end=' ')
            if(c==3):
                print("HUNDRED AND",end=' ')
            if(c==4):
                print("THOUSAND")
        elif(c==2 or c==5 or c==7 or c==9):
             if(b==1):
                print("TEN",end=' ')
             if(b==2):
                print("TWENTY",end=' ')
             if(b==3):
                print("THRITY",end=' ')
             if(b==4):
                print("FOURTY",end=' ')
             if(b==5):
                print("FIFTY",end=' ')
             if(b==6):
                print("SIXTY",end=' ')
             if(b==7):
                print("SEVENTY",end=' ')
             if(b==8):
                print("EIGHTY",end=' ')
             if(b==9):
                print("NINETY",end=' ')
        d=d//10
        c=c-1
            
            
            
