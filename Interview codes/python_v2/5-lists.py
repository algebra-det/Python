thislist = ["apple", "banana", "cherry", "kiwi", "melon"]
print(thislist)

print thislist[2]

print thislist[-1]
print thislist[2:4]
print thislist[:4]
print thislist[2:]
print thislist[-4:-1]

# Appending a list
thislist.append("mango")
print thislist

# Getting index
print thislist.index("mango")

# inserting at a certain index
thislist.insert(1, "orange")
print thislist

# Changing a value
thislist[1] = "blackcurrent"

# removing an element
thislist.remove("banana")
print thislist

# POP , will pop the last element out of the list
thislist.pop()
print thislist

# DEL
del thislist[0]
print thislist

# deleting whole list
# del thislist

# List can have different type of values
thislist1 = ["apple", "banana", 76, "cherry"]
for i in thislist1:
    print type(i)

# Copying a list
newlist = list(thislist)
print newlist


# Joining two or more lists
newest_list = newlist + new_list
print newest_list


# Using list constructor
list1 = list(("apple", "banana", "cherry", "blackforest"))
print list1

list1.sort()
print list1

list2 = sorted(list1)
print list2

"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
