

def great():
    print("Welcome Costumer")
    print("hello")
    print()


great()

def add(x,y):
    c = x+y
    print("Adding Both :",c)

add(4,5)

def add_sub(x,y):
    c = x+y
    if x>=y:
        d = x-y
    else:
        d = y-x

    return c,d

sum , dif = add_sub(4,5)
print("Their sum is ",sum,"\nDifference is ",dif)

