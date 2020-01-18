#seive algorithm for prime number

from time import *
from math import *
t = time()
numbers = list(range(2,1000))
for i in range(2,int(ceil(sqrt(1000)))):
        if i in numbers:
            for j in range(i*2,numbers[-1]+1,i):
                if j in numbers:
                    numbers.remove(j)

print(numbers)
print(len(numbers))
print(time()-t)
