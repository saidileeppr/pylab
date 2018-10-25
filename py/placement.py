a=input("Enter:")
for i in a:
    if(ord(i)<107):
        print(chr(ord(i)+16),end='')
    else:
        print(chr(ord(i)-10),end='')
    
