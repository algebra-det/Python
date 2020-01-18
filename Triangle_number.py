from math import *
from time import *

x = int(input("Enter any number"))
t = time()
for i in range(1,x+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("Execution time :",time()-t)
