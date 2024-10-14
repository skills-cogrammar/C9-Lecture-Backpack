'''
Lists in python.
'''

# Accessing
my_list = ['Bonaventure', 'Dan', 'Armand']
result = my_list[0]
print(result)

# Adding
my_list.append('Bongani')
print(my_list)
# You can use the insert() method

# Remove
my_list.pop()
# You can use the remove method
print(my_list)

# Slicing
sub_list = my_list[:2]
print(sub_list)


# Changing/Manipulating values
my_list[0] = 'Bongani'