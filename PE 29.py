import time
t = time.time()

lst = []

for a in range(2,101):
    for b in range(2,101):
        c = a**b
        if c not in lst:
            lst.append(c)

print(len(lst))

print(time.time()-t)