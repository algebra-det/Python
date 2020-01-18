from time import *
start_time = time()

def next(x):
        if x%2==0:
            return x//2
        else:
            return 3*x+1

z = 0
for x in range(1,1000000,2):
    a = x
    y = 1
    while x>1:
        x = next(x)
        y+=1
    if y>z:
        z = y
        print("At %d with chain length %d" % (a, z))

print(time()-start_time)