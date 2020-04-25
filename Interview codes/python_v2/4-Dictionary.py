content = {
    "showroom": "Kabir Honda",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

content["hero-hai"] = "My name is Akash"

# to get value of a key
x = content.get('hero-hai')
#OR
x = content['hero-hai']

# To print all keys
for y in content:
    print y

print ""

# To print all values
for z in content.values():
    print z

print ""

# To print keys and values
for m,n in content.items():
    print m, " = ",n

print ""

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
# OR
newest_dict = dict(thisdict)
print newest_dict


# Nested Dictionary
thatdict = {
    "child1": {
        "name": "Akash",
        "year": 1997
    },
    "child2": {
        "name": "Mickey",
        "year": 1998
    }
}
print thatdict


# Creating two independent dictionaries annd than creating a single that will contain the two
childish1 = {
    "name": "Akash",
    "year": 1997
}
childish2 = {
    "name": "Mickey",
    "year": 1998
}

family = {
    "child1": childish1,
    "child2": childish2
}
print family


"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
