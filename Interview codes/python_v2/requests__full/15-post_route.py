import requests

# Use post to transfer some data from any "form/inputs in the html page" to the url
# You have to check the html code for the "name"

response = requests.post("http://httpbin.org/post", data={'username': 'akash', 'password': 'testing'})

print type(response.text)   #  It's a unicode i.e. string

# We get the JSON response, so instead of using .text
# We can use json methods

# This will return a dictionary
response_dict = response.json()
"""
This is similar to using a json file, and then using json.load() to convert it into a dictionary
"""

print response_dict
print type(response_dict)       # Dictionary

print response_dict['form']
