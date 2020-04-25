from datetime import datetime

# strptime() only works with datetime

# Using a simple string with space-seperated elements
date_string = "25 April, 2020"
print "date_string = ", date_string

# Converting the given string into a datetime format
# By assigning the space-seperated elements to a given parameters of teh datetime
date_object = datetime.strptime(date_string, "%d %B, %Y")
print "date_object = ", date_object
