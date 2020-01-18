
limit=int(input("Enter ending value for fibonacci series :- "))
x=0
y=1
z=0
sum=0

from array import *
arre = array('i',[])                #for even
arro = array('i',[])
while z<limit:
    z=x+y
    if z>=limit:                  #it will not print the value of z if its value exceeds 4 million
        break
    print(z)

    if z%2==0:
        sum+=z
        arre.append(z)
    else:
        arro.append(z)

    x=y
    y=z

print("Even numbers are :- ")
for i in arre:
    print(i,end=",")
print()

print("Odd numbers are :- ")
for i in arro:
    print(i,end=",")
print()
print("The sum of even fibonacci series is ",sum)
print("Bye")
