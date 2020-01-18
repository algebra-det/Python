#We want to print values which are not divisible by 3

for x in range(1,21):
    if x%2!=0:
        continue
    print(x)
print("bye")

#OR

y=1
while y<=20:
    y+=1
    if y%2!=0:
        continue                        #|continue skips the statement
    print(y)                            #|

print("bbye")

"""And We can use 'pass' """

for i in range(1,21):
    if i%2!=0:
        pass                            #pass is used to just do nothing while 'continue' goes on with the next loop iteration
    else:
        print(i)

print("bbbye")

""" Go to internet to find the difference between continue and pass

    conitinue will skip the whole statement it has under it
    pass will just pass itselt and goes to the next line

"""