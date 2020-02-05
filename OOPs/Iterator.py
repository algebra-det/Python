ls = [6,9,7,2,5,3]

print(ls[2])
print(ls[5])
print()

for i in ls:
    print(i)

print()

it = iter(ls)
print(it)
print(it.__next__())
print(it.__next__())
#or
print(next(it))
print(next(it))
print()
for j in it:        # it will print the rest of the "it" elements left
    print(j)
print()


class topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):         # it will give you the object for iterator
        return self

    def __next__(self):         # it will give the next value or object
        val = self.num
        self.num +=1
        return val
    """ Both __iter__() and __next__() are used to make an ietrable object"""
values = topten()

print(values.__next__())
print(values.__next__())
print(next(values))
print(next(values))
print()

#for k in values:           #it will go on till infinity
#    print(k)

class topte1(topten):

    def __next__(self):
        if self.num <=10:           # this will stop the iteration after 10
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration

tero = topte1()
print(tero.__next__())
print(tero.__next__())
print(next(tero))
print(next(tero))

for k in tero:
    print(k)