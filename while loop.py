print("1st time")
print("1st time")

i = 1                               #initialization

while i<=5:                         #condition
    print("2nd time" , i, "hello")             #that's one more way to print variable values without using "%d"
    i+=1                            #increment/decrement

j = 5                               #initialization

while j>=0:                         #condition
    print("3rd time j is %d"%j)
    j-=1                            #decrement


"""     k = 1
        l = 2
        while k<=3:
            print("the value of k is ", k, end=" ")       #this "end=" is used to exclude the new line function which hapens when there is a new print statement

            while l>=1:
            print("and not ", l, end="")
            l-=1
        k+=1
        print()
        
#This above code will give you result
the value of k is% and not % and not % and not %
the value of k is%
the value of k is%

"""

k = 1
while k<=3:
    print("the value of k is ", k, end=" ")       #this "end=" is used to exclude the new line function which hapens when there is a new print statement
    l = 2
    while l>=1:
        print("and not ", l, end="")
        l-=1
    k+=1
    print()

""" the above code will give:-

    the value of k is  1 and not  2and not  1
    the value of k is  2 and not  2and not  1
    the value of k is  3 and not  2and not  1

"""

# Try to get a hang of this difference in where we have placed
# the l=2 statement
# Do some by checking the debugging feature of this pycharm