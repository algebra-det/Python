import requests
from requests.exceptions import HTTPError
response = requests.get('http://api.github.com')


for x in range(1,11):
    print repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4)

print "{1} and {0}".format("Spam" , "eggs")

x = 9
print type(x)
print type(repr(x))
