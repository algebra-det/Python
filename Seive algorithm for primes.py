from time import time
from math import *

x = int(input("Enter the last number "))
t = time()

lst = list(range(2,x))
for i in range(2,ceil(sqrt(x))):
    if i in lst:
        print(i)
        for j in range(i*2,lst[-1]+1,i):
            if j in lst:
                lst.remove(j)

print(lst)
print("Total Numbers of primes under %d is %d"%(x,len(lst)))

#for k in lst:
#    print(k)

print(time()-t)