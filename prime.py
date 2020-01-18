x=int(input("Enter the number"))


for y in range(1,x+1):
    if x%y==0:
        print(y)
        for z in range(2,y):
            if y%z==0:
                break
        else:
            print(y," is prime")


