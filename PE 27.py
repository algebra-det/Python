#x = int(input("ENter the limit - "))

from time import time
from Seive import seive

t = time()
lst = seive(10000)

def for_41(x):
    new_lst = []
    for i in range(0,x+1):
        j = i*i + i + 41
        if j in lst:
            new_lst.append(j)
        else:
            break
    print(new_lst)
    print(len(new_lst))

def for_79(x):
    new_list = []
    for i in range(0,x+1):
        j = i*i - 79*i +1601
        if j in lst:
            new_list.append(j)
        else:
            break
        print(new_list)
        print(len(new_list))

def for_primes(a,b):
    new_list = []
    for i in range(0,1000):
        j = i*i +a*i + b
        if j in lst:
            new_list.append(j)
        else:
            print("%d with %d gives primes upto %d terms"%(a,b,len(new_list)))
            print(new_list)
            break
    return new_list

y = []
z = 0
q = 0
for i in range(-1000,1000,1):
    for j in range(-1000,1000,1):
        k = for_primes(i,j)
        if len(k) >len(y):
            y = k
            print("As %d and %d "%(i,j))
            z = i
            q = j

print("As %d and %d with total %d number of consecutive primes "%(z,q,len(y)))
print("Product of %d and %d is %d "%(z,q,z*q))
print(y)
print(time()-t)








