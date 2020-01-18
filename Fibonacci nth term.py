nth = int(input("Enter the series nth"))

def fibonacci():
    x = 0
    y = 1
    for i in range(nth):
        z = x+y
        x = y
        y = z
        print(z)

fibonacci()