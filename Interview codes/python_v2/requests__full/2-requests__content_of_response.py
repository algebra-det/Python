
import requests

response = requests.get("https://api.github.com")

# It returns a string , it's in RAW bytes
content = response.content

print content
print type(content)

print ""

# Converting the response into a json which is much more like a dictionary
content3 = response.json()
for key, value in content3.items():
    print (key, " = ", value)
