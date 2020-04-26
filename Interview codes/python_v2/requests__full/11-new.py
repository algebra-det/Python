import requests

response = requests.get("https://xkcd.com/353/")

print response

# print dir(response)
# print help(response)

# To get the url
print response.url

# to get the content of the response in unicode
# i.e. for our page, we will get the whole HTML content,  OR you will get the source of the website
print response.text
