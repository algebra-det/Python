x = 0

for i in range(1,200):
    s = str(i)
    for j in s:
        if j == "1":
            x+=1

print(x)