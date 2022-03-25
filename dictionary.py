from unicodedata import name


# Duplication not allowed of data 

my_dict = {
    'name': 'saljesh',
    'name': 'Success',
    'age': 21,
    'is_tall': True,
    'nationality' : 'African',
    'friends': ['Peter', 'alien', 'Gwara']
}

print(my_dict['name'])
print(len(my_dict))
print(type(my_dict['friends']))
print(type(my_dict))


x = my_dict['name']

print(x)