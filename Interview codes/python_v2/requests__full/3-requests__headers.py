import requests

response = requests.get("https://api.github.com")

# It by default returns a dictionary
header = response.headers

print type(header)

print header['content-type']

header['hero-hai'] = "My Name Is Akash"

# to get value of a key
x = header.get('hero-hai')
#OR
x = header['hero-hai']

# To print all keys
for y in header:
    print y

print ""

# To print all values
for z in header.values():
    print z


# To print keys and values
for m,n in header.items():
    print m, " = ",n


# Deleting items from the dictionary
thisdict = {
    "showroom": "Kabir Honda",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print thisdict

# Deleting Using Functions
thisdict.pop("model")
print thisdict

# Deletes the last inserted item
thisdict.popitem()
print thisdict

# Deleting Using keyword
del thisdict["brand"]
print thisdict

# Del can also delete the whole dictionary
del thisdict
# print thisdict    --> this will resutl in an ERROR : "thisdict" is not defined

# Again
thisdict = {
    "showroom": "Kabir Honda",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print thisdict

# To empty the dictionary
thisdict.clear()
print thisdict


# Again
thisdict = {
    "showroom": "Kabir Honda",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print thisdict

# To copy a dictionary
# We cannot a dictionary by
# new_dict = thisdict
# Because it will just be a reference to the address to thisdict's address

new_dict = thisdict.copy()
print new_dict
