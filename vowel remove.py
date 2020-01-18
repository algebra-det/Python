x = input("Enter the string - ")
y = "aeiou"
z = []
for i in x:
    if i in y:
        pass
    else:
        z.append(i)
for j in z:
    print(j,end="")

print()

s = input('Enter any string to remove all vowels from it: ')
vowels = 'aeiou'
s =s.replace(s[0],s[0].upper())
print(s)
s = s.lower()
for x in s:
   if x in vowels:
       s = s.replace(x, "")   # Replacing the vowels with ‘’
print(s)