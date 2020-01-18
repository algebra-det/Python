
def prime(x):
    for z in range(2,x):
        if x%z==0:
            print("its divisible by",z)
            print("Not prime")
            break
    else:
        print("Its prime\nHence divisible by itself only")

def primeif(x):
    for i in range(2,x):
        if x%i==0:
            pass
    else:
        print(" It's prime")

def main():
    x = int(input("enter the number"))
    prime(x)

if __name__=="__main__":
    main()


