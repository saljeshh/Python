# A list is a collection which is ordered and changable. Allows duplicate members.

# Create List
numbers = [1,2,3,4,5]
fruits = ['Apples','Oranges','Grapes','Pears']

# Use a constructor
numbers2 = list((1,2,3,4,5))

# Print the lists
print(numbers)
print(fruits)
print(numbers2)

# Get a value
print(fruits[1])

# Get the last value
print(fruits[-1])

# Get  length of list
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2,'strawberries')
print(fruits)

# Change values
fruits[2] = 'Berries'
print(fruits)

# Remove with pop
fruits.pop(0)
print(fruits)

# Reverse List
print("Reversed....")
fruits.reverse()
print(fruits)

# Sort List
print("sorted...")
fruits.sort()
print(fruits)

# Reverse sort
print("Reveresed again...")
fruits.sort(reverse=True)
print(fruits)


#  =============
print('\n\n\n')
countries = ['United Kingdom', 'Ghana', 'Nigeria', 'Australia']
print(countries)

# gets the first letter of the list
print(countries[2][0])

# get only list from ghana to austraila
print(countries[1:])
print(countries[2:])

# Replaced US with uk
countries[0] = 'united states'
print(countries)

name = 'tomi'
print(type(name))

# print last
print(countries[-1])

