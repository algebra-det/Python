""" Generator gives us iterators
    to make iterator we have to define two methods i.e. __iter__() and __next__()
    but is we want python to automatically define us both methods we have generators to do so"""

""" return terminates the function while yield don't """

def topten():
    return 1

val = topten()
print(val)
# print(val.__next__())     #next don't work with normal functions and do not work with 'return'

def top():
    yield 1
    yield 2
    yield 3
    yield 4

bal = top()
print(bal)
print(bal.__next__())
print(next(bal))
for j in bal:
    print(j)

# lets make this function that gives top ten perfect squares
def ter():

   i = 1

   while i<=10:         # we can't use for loop as it works on iterables , here we are making iterable
       sq = i*i         # we used 10 to have maximum 10 values, otherwise it will go on till infinity
       yield sq
       i+=1

rot = ter()
print(rot)
print(rot.__next__())
print(next(rot))
for k in rot:
    print(k)

""" return terminates the function while yield don't
    hence, we can make iteration by using yield
    'return' terminates the function hence when we call it again it will start from scratch
    'yield' dont terminate the function and pauses it in the current state and hence we can
    continue the iteration
    
    We are making an iterator using a GENERATOR """



