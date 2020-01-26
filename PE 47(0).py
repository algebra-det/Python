primes = [2]
import time
start = time.time()
def prim(n,primes): #makes a list of primes
    for i in range(0,len(primes)):
        if n%primes[i] == 0:
            return False

for i in range(2,10000): #checks if numbers are prime
    if prim(i,primes) == None:
        primes.append(i)

def fac(n,primes):
    factors = []
    for i in range(0,len(primes)):#creates a list of prime factors
        if n%primes[i] == 0:
            n = n/primes[i]
            factors.append(primes[i])
    return factors

for j in range(0,1000000): #checks for 4 consecutive numbers with 4 prime factors
    list = fac(j,primes)
    if len(list) == 4:
        list = fac(j+1,primes)
        if len(list) == 4:
            list = fac(j+2,primes)
        if len(list) == 4:
            list = fac(j+3,primes)
            if len(list) == 4:
                print(j)
                print ('In ' + str(time.time()-start) + ' seconds')
                break
