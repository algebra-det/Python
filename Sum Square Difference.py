
a = int(input("Enter the number of natural numbers "))

def Difference(a):
    x = 0
    y = 0
    for i in range(1,a+1):
        x += i*i
    print("Sum of Squares is : ")

    for i in range(1,a+1):
        y+=i
    z = y**2
    print("Square of Sum is : ")

    return x,z

sum,square = Difference(a)
print("Difference is :- ",abs(sum-square))

""" 
    abs() is a built-in function which converts 
    negetive number into positive %
    positive numbers remain unchanged
    As in above we want the difference so it Does't matter
    if it's negetive of positive 
    as the difference is always postive no matter from where to where
    Hence, we used this abs() function
"""