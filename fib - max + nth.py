x = int(input("Enter the ending digits"))

def fib(x):
    y = 0
    z = 1
    a = 0
    while a<x:
        a = y+z
        if a>=x:
            break
        print(a)
        y = z
        z = a

fib(x)

y = int(input("Enter the nth term"))

def fibo(y):
    x = 0
    y = 1

    for i in range(globals()['y']):
            z = x+y
            print(z)
            x = y
            y = z

fibo(y)