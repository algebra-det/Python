import requests

response = requests.get("https://imgs.xkcd.com/comics/python.png")

print response.status_code
print response.ok


print response.headers
