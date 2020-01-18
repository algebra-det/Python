
class fibonacc:

    def fibonacci(self,f):
        x = 0
        y = 1

        for i in range(f):
            z = x + y
            x = y
            y = z
            print(z)

hero = fibonacc()

nth =int(input("fibonacci series upto how many terms "))

hero.fibonacci(nth)

#OR
print()
class fibona:

    def fibonaccies(f):
        x =0
        y = 1
        for i in range(f):
            z = x + y
            x = y
            y = z
            print(z)

ntth = int(input("ENter the series upto"))
fibona.fibonaccies(ntth)
print()

#OR


class fibonaccie:

    def __init__(self,f):
        self.f = f

    def fib(self):
        y = 0
        z = 1
        a = 0
        while a < self.f:
            a = y + z
            if a >= self.f:
                break
            print(a)
            y = z
            z = a

    def fibonacci(self):
        x = 0
        y = 1

        for i in range(self.f):
            z = x + y
            x = y
            y = z
            print(z)

nttth = int(input("Enter the series upto"))
fib2 = fibonaccie(nttth)                            # Object with one variable f
fib2.fibonacci()                                    # calling method fibonacci() for fib2 object

y = int(input("Do you want to have a series of upto any specified number ? if yes then press 1 "))
if y == 1:
    x = int(input("Enter the ending digits"))
    fib3 = fibonaccie(x)                                # Object with one variable f
    fib3.fib()                                          # calling mehtod fib() for fib3 object
else:
    pass
