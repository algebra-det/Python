# A function without name is called anonymous function or Lambda
# We use lambda where we want to have a function for single use

def square(a):
    return a*a

print(square(5))

f = lambda a:a*a                    #Just One Line
                                    # Lambda functions must have
                                    #only one explanation
result = f(5)
print(result)


g = lambda a,b:a+b

result1 = g(3,5)
print(result1)
