

def fibonacci(n):
    x = 0
    y = 1
    print("1  at  1")
    for i in range(2,10000):
            z = x + y
            x = y
            y = z
            print(z," at ",i)
            a = str(z)
            if len(a)==n:
                print("So %d Digits is at "%n,i)
                break

def main():
    n = int(input("Enter the number of digits in fibonacci series you want to find out : "))
    fibonacci(n)

if __name__=="__main__":
    main()