from math import *
from time import *
t = time()

def factors(x):
    fact =0
    for j in range(1,ceil(sqrt(x))):
        if x%j==0:
            fact +=2
    return fact

x=0
for i in range(1,800000):
    x +=i
    print(x)
    if factors(x) >= 500:
        print(x)
        break

print(time()-t)
