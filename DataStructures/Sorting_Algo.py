
def minimum(li):
    min = li[0]
    for i in li:
        if i<min:
            min = i
    return min


li = [5,7,9,3,1,5,4]

length = len(li)
new = []

i = 0
while i<length:
    j = minimum(li)
    li.remove(j)
    new.append(j)
    i+=1

print(new)

#OR

li = [99,8,12,4,45,7]

new = []
for i in range(len(li)):
    j = minimum(li)
    new.append(j)
    li.remove(j)

print(new)


