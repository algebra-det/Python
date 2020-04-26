import uuid

var = uuid.uuid4()

# To get the "Hardware address" , a 48-bit positive integer
print uuid.getnode()

print uuid.uuid1()

# It will be same every time
print uuid.uuid3(var, 'akash')

print uuid.uuid4()
