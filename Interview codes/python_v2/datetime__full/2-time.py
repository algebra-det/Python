from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print "a = ",a

# time(hour, minute and second)
b = time(11, 34, 56)
print "b = ",b

# time(hour, minute and second)
c = time(hour=11, minute=34, second=56)
print "c = ",c

print "hour = ", c.hour
print "minute = ", c.minute
print "seconds = ", c.second
print "microseconds = ", c.microsecond
