
y = []
x = int(input("Enter the decimal number "))
def binary(x):
    while x>=1:
        z = x%2
        x = x//2
        y.append(z)
    b = reversed(y)
    print("Binary :- ",end="")
    for i in b:
        print(i,end="")
    print()

def octal(x):
    while x>7:
        z = x%8
        x = x//8
        y.append(z)
    b=reversed(y)
    print("Octal :- ",end="")
    print(x,end="")
    for i in b:
        print(i,end="")
    print()

def hexa(x):
    while x>15:
        z = x%16
        x = x//16
        if z==10:
            z = 'A'
            y.append(z)
        elif z ==11:
            z = 'B'
            y.append(z)
        elif z ==12:
            z = 'C'
            y.append(z)
        elif z ==13:
            z = 'D'
            y.append(z)
        elif z==14:
            z = 'E'
            y.append(z)
        elif z ==15:
            z = 'F'
            y.append(z)
        else:
            y.append(z)
    b = reversed(y)
    print("Hexadecimal :- ",end="")
    print(x,end="")
    for i in b:
        print(i,end="")
    print()

binary(x)
print("\t\t",bin(x))

y=[]
octal(x)
print("\t\t",oct(x))

y=[]
hexa(x)
print("\t\t",hex(x))
