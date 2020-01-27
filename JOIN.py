
lst = [1,6,5,48,9,2,3,65,4,2,0]
lst2 = list(map(str,lst))
print(lst2)
b = ''
b = b.join(lst2)
print(b)
print(type(b))

print()

#OR

print("".join(lst2))