import datetime

# Getting current date and time
datetime_object = datetime.datetime.now()
print datetime_object


# Getting Current date
date_object = datetime.date.today()
print date_object

# To get all the classes of this datetime module
print dir(datetime)


# Creating custom date object/instance
d = datetime.date(2020, 05, 25)
print d


# Getting date from a timestamp
# A Unix timestamp is the number of seconds between a particular date and
# January 1, 1970
timestamp = datetime.date.fromtimestamp(1326244364)
print "date = ", timestamp


# Printing today's year, month and day
today = datetime.date.today()
print today.year
print today.month
print today.day


# Getting all methods of date class
print dir(datetime.date)
