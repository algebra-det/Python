x=0
for i in range(2,2000000):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        x+=i

print(x)
