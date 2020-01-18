#starting with 1


y = int(input("Enter the n'th term : "))
x = []
for j in range(1,1000000):
    if x.__len__()>=y:
        break
    else:
        for k in range(2,j):
            if j%k==0:
                break
        else:
            print(j)
            x.append(j)

print("The %d'st prime number is %d"%(y,x[x.__len__()-1]))