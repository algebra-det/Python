from Triangle_number import triangle
import numpy

tri = triangle(1000)


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
al = {}
for i in range(len(alpha)):
    al[alpha[i]] = i+1

print(al)