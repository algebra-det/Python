from Digit_Fibonacci_at import fibonacci


def newfibo(func):
    def inside(n):
        if n>10:
            print("So you want it to be greater")
        return func(n)
    return inside

fibonacci = newfibo(fibonacci)
fibonacci(122)