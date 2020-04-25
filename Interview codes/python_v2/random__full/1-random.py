import random

# Random float between 0-1
print random.random()

# Random Integer between specified integers
x = random.randint(1,100)
print x

# Random element from the range created by start, stop and step arguments
y = random.randrange(1,100,2)
print y

# Random element from a non-empty sequence
z = random.choice([12,345,456,675,7355,53])
print z

m = random.choice("Computer")
print m

# Shuffle randomly / Randomly reorder
numbers = [12,234,345,3,54,6,3542,53]
print numbers
random.shuffle(numbers)
print numbers
