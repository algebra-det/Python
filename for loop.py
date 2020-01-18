# FOR loop

x = ['akash', 22 , 1997]

for i in x:                 #for loop don't take conditions
    print(i)

y = "akash"
for j in y:
    print(j)

# OR

print()

for k in "akash":           #we can give values in "for" itself without taking any other variable
    print(k)                #Hence saving memory

for l in ["akash", 22, 1997]:
    print(l)


for m in range(10):             #remember range starts from zero by default
    print(m)                    #and it goes till 1 less ending point

print()
for m in range(10,20):          # iin here ending will terminate at 19
    print(m)

for m in range(20,40,2):        #starting point, ending point, difference,iteration
    print(m)

for m in range(21,11):          #this will not work
    print(m)
"""to make the above code work we have to give -1 as iteration"""

for m in range(21,11,-1):       #now it will work
    print(m)


for m in range(10):             #from (0-9)
    if m%5!=0 :                 #will exclude values which are divisible by 5
        print(m)
