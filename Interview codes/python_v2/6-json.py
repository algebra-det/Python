import requests, json

# Some Jsono
x = '{ "name": "akash", "age":30, "city":"new york"}'

# This will parse x , AND result into a dictionary, here y is a dictionary now
y = json.loads(x)
print y
print type(y)




response = requests.get("https://api.github.com")

# It returns a string , it's in RAW bytes
content = response.content

print type(content)

print ""


# As the content is in string format but is structured as a dictionary json, we can convert the content into json ...dictionary
json_content = json.loads(content)
print json_content["user_repositories_url"]
print type(json_content)

print ""
# Converting dictionary into a JSON String
# Some Dictionary
m = {
    "name": "john",
    "age": 30,
    "city": "New york"
}

# Converts into JSON Strings
n = json.dumps(m)
print n
print type(n)

print ""
# You can convert any type of objects into JSON strings


print json.dumps({"name": "akash", "age":22})
print type(json.dumps({"name": "akash", "age":22}))
print ""
print json.dumps(["apple", "banana"])
print type(json.dumps(["apple", "banana"]))
print ""
print json.dumps(("apple", "banana"))
print type(json.dumps(("apple", "banana")))
print ""
print json.dumps("hello")
print json.dumps(45)
print json.dumps(True)
print type(json.dumps(True))
print json.dumps(False)
print json.dumps(None)




# All in one
x = {
    "name": "akash",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg":244.1}
    ]
}

print json.dumps(x)
print type(json.dumps(x))
print ""

# To have a sort and easy understandable display of the json
print json.dumps(x, indent=4, sort_keys=True)
