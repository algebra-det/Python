x = input("Enter first number ")
y = input("Enter second number ")

#By default the input() gives you values in string format
""" So we have to convert the string values into integer format"""

print("the type of input is always %s"%type(x))
a = int(x)
b = int(y)

z = x + y
w = a + b
print(z)
print("the values you entered are (in string):-\nx = %s\ny = %s"%(x,y))
print("the values you entered are (in integer):-\nx = %d\ny = %d"%(a,b))
print("the sum of your entered values is in string %s"%z)
print("the sum of your entered values is %d"%w)

"""As you can see that there is extra variables needed for this
    simple code, which means memory is wasted
    
    so instead of using a and b for putting integer values of
    user's input data
    
    we can use "int" in the first variable"""


j = int(input("\n\n\n\n\nEnter third number "))
k = int(input("Enter fourth number "))
# here the values will be directly stored in integer format as
# the default 'input()' takes values in string format

l = j*k

print("The values your secondly entered are %d and %d"%(j,k))
print("The into of the given input is")
print(l)

 # Now we will have take our inputs in character format

ch = input("Enter any character -ch = ")
print(ch)
"""As you know it will print the whole characters the user is 
    entering 
    for example,
            if he is typing  "c" than output will be "c"
            if he is typing "cartoons" than the output will be "cartoons"
            
    so in order to take only the character
    we can use the addressing system i.e. 
    by using [0] for first chracter
    by using [1] for second and so on"""

print(ch[0])

#or we can define in the input to fetch only one character
#i.e. by using [0] in input

r = input("Enter any character -r = ")[0]     #its awesome
print(r)

""" There is a function to evaluate the given input 
    for example,
        if the input given by user is '5+9-1' 
        SO it will evaluate the input
        try to give this value in 'r' """

p = eval(input('Enter the expression again -p ='))
print(p)
