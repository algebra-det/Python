from datetime import date, datetime, timedelta

t1 = date(year=2018, month=12, day=23)
t2 = date(year=2019, month=3, day=24)
t3 = t2 - t1
print "t3 is ",t3
print type(t3)


t4 = datetime(year=2018, month=12, day=23, hour=18, minute=56, second=12)
t5 = datetime(year=2020, month=2, day=24, hour=13, minute=34, second=57)
t6 = t5 - t4
print "t6 is ",t6

t7 = datetime.now() - t4
print "t7 is ",t7


# In TimeDelta there's 's' as suffix in weeks, days, hours, etc
t8 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t9 = timedelta(days=4, hours=11, minutes=4, seconds=12)
t10 = t8-t9
print "t10 is ",t10

# This will be negetive as the date is being subtracted from lower date
t11 = t9 - t8
print "t11 is ",t11
print "negetive t11 now is ", abs(t11)

print "t12(-ve) is ", (timedelta(seconds=33) - timedelta(seconds=55))
print "t12(+ve) is ", abs((timedelta(seconds=33) - timedelta(seconds=55)))


# Time duration in total seconds
t13 = timedelta(days=5, hours=1, minutes=45, seconds=12)
print "t13 in total seconds is ", t13.total_seconds()
