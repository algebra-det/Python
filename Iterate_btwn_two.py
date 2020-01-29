players = [1,0]

choice = 1
for _ in range(10):
    current_player = choice
    print(current_player)
    choice = players[choice]

print("val")

#OR

val =1
for _ in range(10):
    val = 1 -val
    print(val)

print("itertools 1")
# OR using itertools import cycle

from itertools import *

myIterator = cycle(range(2))
for  _ in range(10):
    print(myIterator.__next__())

print("itertools 2")
#OR
for _ in range(10):
    print(next(myIterator))

for char in "hello my name is akash chauhan":
    print(char,end=",")
print()

x = [1,2,3,4]       # iterable

n = cycle(x)        # iterator! ..also iterable , iterator are the object which work on iterableef

y = iter(x)         # iterator! ..also iterable

