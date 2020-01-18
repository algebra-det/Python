""" In this code, if the required candies exceeds the available candies
    than it will give all the candies it have and then stop """

av = 4              #available candies
u = int(input("Enter the number of candies you want again"))
o = 1
while o<=u:
    if o>av:
        break                           #'break' means 'just jump out of the loop'
    print("second another one")
    o+=1

print("bye")

#OR

p = 1
while p<=u:
    if p>av:
        print("Out Of Stock")
        break
    else:
        print("third another one")
        p+=1

print("Bye Again")

for q in range(u):
    if q>=av:                           # there is equal to "=" because range starts with 0
        print("Out Of Stock")
        break
    print("there you go candies")

print("BBBBye")