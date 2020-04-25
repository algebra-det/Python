from datetime import datetime
import pytz

"""
Suppose we are working on a project and need to display date and time based on their timezone
Rather than trying to handle timezone yourself, we should use a third-party 'pytz' module
"""

local = datetime.now()
print "local: ", local.strftime("%m/%d/%Y, %H:%M:%S")

tz_IN = pytz.timezone("Asia/Calcutta")
print type(tz_IN)
datetime_IN = datetime.now(tz_IN)
print "IN: ", datetime_IN.strftime("%d/%m/%Y, %H:%M:%S")


tz_NY = pytz.timezone("Europe/London")
datetime_NY = datetime.now(tz_NY)
print "NY: ",datetime_NY
