from array import *

def fibonacci():
    p = int(input("Enter ending value for fibonacci series :- "))

    x=0
    y=1
    z=0
    sum=0

    arrz = array('i',[])
    arre = array('i',[])                #for even
    arro = array('i',[])
    while z<p:
        z=x+y
        arrz.append(z)
        if z>=p:                  #it will not print the value of z if its value exceeds 4 million
            break

        if z%2==0:
            sum+=z
            arre.append(z)
        else:
            arro.append(z)

        x=y
        y=z
    printing(arrz, arre, arro, sum)

def printing(j,k,l,m):
    for a in j:
        print(a)
    print()
    print("Even numbers are :- ")
    for i in k:
        print(i,end=",")
    print()

    print("Odd numbers are :- ")
    for i in l:
        print(i,end=",")
    print()
    print("The sum of even fibonacci series is ",m)
    print()
    ask = input("Do you want another fibonacci series ? yes/no :- ")
    if ask == 'yes':
        fibonacci()
    else:
        print("OK\nBBYE")

if __name__=="__main__":
    fibonacci()

print()
print()

