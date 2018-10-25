#AIM:TO DEMONSTRATE STRING METHODS
st="welcome to python"
s="Ab9"
s1="Ab"
s2="908"
s3="    "
ss="wel"
ss1="on"
st1=r"wel\ncome\t"
l=st.split(" ")
print(s1+s2)
print(st.upper())
print(st.lower())
print(st.title())
print(st.swapcase())
print(s.isalnum())
print(s1.isalpha())
print(s2.isdigit())
print(st.istitle())
print(st.isupper())
print(st.islower())
print(s3.isspace())
print(st1)
print(st.find("o"))
print(st.index(ss))
print(st.rfind(s1))
print(st.rindex(ss1))
print(st.count("o",0))
print(st.split(" "))
print("-".join(l))
print(st.startswith(ss))
print(st.endswith(ss1))
print(len(st))
print(s*2)
print(st.replace("pyton","c"))
"""
INPUT/OUTPUT:
Ab908
WELCOME TO PYTHON
welcome to python
Welcome To Python
WELCOME TO PYTHON
True
True
True
False
False
True
True
wel\ncome\t
4
0
-1
15
3
['welcome', 'to', 'python']
welcome-to-python
True
True
17
Ab9Ab9
welcome to c """
