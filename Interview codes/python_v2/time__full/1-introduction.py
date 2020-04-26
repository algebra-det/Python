import time

# EPOCH = For Unix System, January 1, 1970, 00:00:00 at UTC is epoch(The point where time begins).

# Get the number of seconds passed since epoch
seconds = time.time()
print "seconds Passed since epoch: ",seconds


# Get the local time (string format), by passing 'seconds' argument passed  since epoch
local_time = time.ctime(seconds)
print "Local Time: ", local_time


# To Suspend (delay) execution of the current thread for the given number of seconds
print "This is printed immediately"
time.sleep(2.4)
print "This is printed after 2.4 seconds"


# Struch_Time class : Several functions in the time module such as gmtime(), asctime(), etc.
# either take time.struct_time object as an argument or return it
# structed_time = time.struct_time(
#     tm_day=2020, tm_mon=4, tm_mday=26,
#     tm_hour=7, tm_min=5, tm_sec=27,
#     tm_wday=4, tm_yday=118, tm_isdst=0
# )
# print structed_time

# FROM EPOCH SECONDS TO LOCAL TIME

# Localtime() : takes number of seconds passed since epoch as an argument and returns struct_time
# in local time
result = time.localtime(seconds)
print "Result: ", result
# print "tm_year: ", result.tm_year
# print "tm_mon: ", result.tm_mon
# print "tm_mday: ", result.tm_mday
# print "tm_hour: ", result.tm_hour
# print "tm_min: ", result.tm_min
# print "tm_sec: ", result.tm_sec
# print "tm_wday: ", result.tm_wday
# print "tm_yday: ", result.tm_yday
# print "tm_isdst: ", result.tm_isdst

# FROM EPOCH SECONDS TO UTC

# Gmtime() : takes number of seconds passed since epoch as argument and returns struct_time
# in UTC
gmtime_result = time.gmtime(seconds)
print "Gmtime_result: ", gmtime_result
print "year: ", gmtime_result.tm_year
print "tm_hour: ", gmtime_result.tm_hour

"""
Local Time Conversion
Ballabhgarh, Faridabad, Haryana is 5 hours and 30 minutes ahead of Coordinated Universal Time
1:48 am Sunday, in Coordinated Universal Time is
7:18 am Sunday, Ballabhgarh, Faridabad, Haryana (IST)
"""

# FROM STRUCT_TIME OR (TUPLE containing 9 elements corresponding to struct_time) TO LOCAL TIME

# MKTIME() : Converting struct time into seconds passed since epoch
m = time.time()             # Getting seconds since epoch
n = time.localtime(m)       # From seconds to local_time
print "n : ", n
o = time.mktime(n)          # From local_time to seconds
print "O : ", o

t = (2020, 4, 26, 7, 35, 23, 4, 118, 0)
local_time_form_mktime = time.mktime(t)
print "Local_time_from_mktime : ", local_time_form_mktime


# FROM STRUCT_TIME OR (TUPLE containing 9 elements corresponding to struct_time)
# TO A STRING REPRESENTING LOCAL TIME
tup = (2020, 4, 26, 7, 35, 23, 4, 118, 0)
result1 = time.asctime(t)
print "Result1 : ", result1
