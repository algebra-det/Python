"""Here we will learn the working of if and else conditions"""


if False:
    print("hello I am here")
print("nothing0")                   #allignment is important
#as it is not alligned so it will not work with if

if False:
    print("As I said I am here")
    print("nothing1")               #here its alligned so it will work along if


x = int(input("Enter any value"))
r = x % 2
s = x % 5

if (r==0):                  #We can use brackets() too
    print("It's EVEN")
    if x>5:
        print("It's greater than 5 too")
    else:
        print("It's not greater than 5")

else:
    print("It's ODD")
    if s==0:
        print("It's divisible by 5")
    else:
        print("It's not divisible by 5")

print("BYE")