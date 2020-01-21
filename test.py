
from math import *

a = []
for i in range(1,1000001):
    j = (i*((3*i)-1))//2
    a.append(j)

print(a)
print(len(a))


for k in range(3,9989):
    for l in range(1,11):
        m = a[k]+a[k+l]
        if m in a:
            print("%d + %d = %d " % (a[k], a[k+l], m))
            n = int(abs(a[k]-a[l]))
            if n in a:
                print("%d + %d = %d with diff %d" % (a[k], a[k+l],m,n ))
