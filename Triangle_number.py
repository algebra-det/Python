
def triangle(x):
    triangles = []
    for i in range(x):
        j = int(((1/2)*i)*(i+1))
        if j<x:
            triangles.append(j)
        else:
            break
    return triangles

def main():
    x = int(input("Enter the Number Upto "))
    print(triangle(x))

if __name__=="__main__":
    main()
