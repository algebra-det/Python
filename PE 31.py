
import time ,math
t = time.time()
#number = int(input("Enter the a number"))
number = list(range(2,int(input("Enter the number"))+1))
i = 2
#from 2 to sqrt(number)
for i in range(2,int(math.sqrt(number[-1]))):
    #if i is in list
    #then we gotta delete its multiples
    if i in number:
        #j will give multiples of i,
        #starting from 2*i
        for j in range(i*2, number[-1]+1, i):
            if j in number:
                #deleting the multiple if found in list
                number.remove(j)

print(number)
print(len(number))
print(time.time()-t)
