import requests

# we can pass the arguments straight to the url like, "https://httpbin.org/get?page=2&count=25"
# Best way to pass arguments is to use "params" with the "dictionary" as argument

payload = { 'page':2, 'count':25}

response = requests.get("https://httpbin.org/get", params=payload)

print response.text

# Now check the url, it will automatically have the arguments in it
print response.url
