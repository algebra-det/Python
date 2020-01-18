# Break                         - Breaks the loop
# Continue                      - Skips the statement and continue with next loop iteration
# Pass                          - As we can't left if statement empty , we use pass statement , it will pass means do nothing

x = int(input("How many candies do you want"))
y = x                           #we gotta use it for our while increment bcs after executing the for and while decrement , the value of x will get 0 so we have to store x's value somewhere for later use
for i in range(x):              #by using for loop
    print("Candies")

#OR
j = 0                           #by using while loop with decrement
while x>j:
    print("\n candies")
    x-=1                        #As here we are decrementinig the original input taken variable , it will become 0 , that's why we took another variable "y" to have the input value for next incremental use

#OR

k = 1
while k<=y:
    print("again candies")
    k+=1                           #by using whileloop with increment



"""This below program will tell the user that the required vandies are not available"""

available = 14                      #lets suppose this is available candies
z = int(input("how many more candies do you want "))
if z<=available:
    for l in range(z):
        print("more candies")

else:
    print("Sorry, but We don't have that much candies available")

m = 1
while m<=z:
        if z <= available:
            print("here you go bro")
            m+=1

        else:
            print("Sorry , but we don't have that much candies available")

n = 1
if z<=available:
    while z>=n:
        print("another one")
        z-=1

else:
    print("Sorry, but we don't have that much candies available")


