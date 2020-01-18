from array import *

x = []
for y in range(10):
    z = input("Enter the name : ")
    x.append(z)

def letters(x):
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    for i in x:
        if len(i)==4:
            a.append(i)
        if len(i)==5:
            b.append(i)
        if len(i)==6:
            c.append(i)
        if len(i)==7:
            d.append(i)
        if len(i)>=8:
            e.append(i)
    return a,b,c,d,e

a,b,c,d,e=letters(x)
print("name containing only 4 letter : ",a)
print("name containing only 5 letter : ",b)
print("name containing only 6 letter : ",c)
print("name containing only 7 letter : ",d)
print("name containing more than 7 letter : ",e)

