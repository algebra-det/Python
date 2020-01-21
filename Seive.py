from time import time
from math import *

def seive(x):
    lst = list(range(2,x))
    for i in range(2,ceil(sqrt(x))):
        if i in lst:
            print(i)
            for j in range(i*2,lst[-1]+1,i):
                if j in lst:
                    lst.remove(j)
    return lst

def main():
    x = int(input("Enter the last number "))
    t = time()
    print(seive(x))
    print(time() - t)

if __name__=="__main__":
    main()

#for k in lst:
#    print(k)
