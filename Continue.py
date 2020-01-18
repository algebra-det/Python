
for x in range(1,101):
    if x%3!=0 and x%5!=0:
        print(x)
print("bye")

# "Break" will break the loop while "continue" will skip the statement

for y in range(1,101):
    if y%3==0 or y%5==0:
        break                    #it will break the loop
    print(y)

print("bbbye")

#Hence we will use 'continue' which will skip the statement if its true
for w in range(1,101):
    if w%3==0 or w%5==0:
        continue                    #it will skip the statement
    print(w)

print("bbye")

#OR

z = 0
while z<=99:
    z+=1
    if z%3==0 or z%5==0:            # if we put and instead of or than it will work only when both are true for example at 15
        continue
    print(z)

print("bbbbbye")