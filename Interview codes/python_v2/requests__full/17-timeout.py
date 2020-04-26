"""
One more thing:
If we run requests, than it will wait until we get a requests,
and it will wait and hangforever
SO to overcome this issue we should :

Set a timeout in our code
"""

import requests

# In below url, delay means it will delay the response by {} seconds
response = requests.get("https://httpbin.org/delay/6", timeout=3)

# as the dealy is 6 seconds, and our timeout is 3-seconds :
# Means:
# the website will return any response in 6 seconds, i.e. wait 6 seconds and then respond
# Our timeout is 3-seconds, as the response will take 6 seconds,
# It will result in timeout and will return an error

print response
