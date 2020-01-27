
#1533776805

from time import time

triangle = []
for i in range(60000):
    j = (i*(i+1))//2
    triangle.append(j)

pentagonal = []
for k in range(40000):
    l = (k*(3*k-1))//2
    pentagonal.append(l)


hexagonal = []
for m in range(30000):
    n = (m*(2*m-1))
    hexagonal.append(n)

print(hexagonal)

print(triangle.index(1533776805))
print(pentagonal.index(1533776805))
print(hexagonal.index(1533776805))

t = time()

from math import sqrt
for x in range(285,100000):
	c = (x**2 + x)/2
	y = (.5 + sqrt(.25 + 6*c))/3
	z = (1 + sqrt(1 + 8*c))/4

	if y - int(y) == 0 and z - int(z) == 0:
		print('x = %d' % x)
		print('y = %d' % y)
		print('z = %d' % z)
print(time()-t)




