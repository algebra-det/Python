fruit = [['Orange', 'Fruit'], ['Banana', 'Fruit'], ['Mango', 'Fruit']]
consume = ['Juice', 'Eat']
possible = []

# Iterating item in list fruit
for item in fruit:

    # Inerating use in list consume
    for use in consume:
        item.append(use)
        possible.append(item[:])
        item.pop(-1)
print(possible)

# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C','HTML','CSS','PHP']
# remove and return the last item
print('When index is not passed:')
print('Return Value:', languages.pop())
print('Updated List:', languages)
# remove and return the last item
print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)
# remove and return the third last item
print('\nWhen -3 is passed:')
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)