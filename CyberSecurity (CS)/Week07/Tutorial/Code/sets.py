# Creating sets
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Using the set() function
my_set = set([1, 2, 3, 4, 5, 5])  # duplicates are ignored
print(my_set)

# Adding elements
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# Removing Elements
my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4}

# Using discard() – won’t raise an error if the item doesn’t exist
my_set.discard(5)  # No error, even though 5 isn't in the set

# Membership check
my_set = {1, 2, 3}
print(2 in my_set)    # Output: True
print(5 in my_set)    # Output: False

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
print(union_set)  # Output: {1, 2, 3, 4, 5}

set_a = {1, 2, 3}
set_b = {3, 4, 5}
intersection_set = set_a & set_b
print(intersection_set)  # Output: {3}

set_a = {1, 2, 3}
set_b = {3, 4, 5}
difference_set = set_a - set_b
print(difference_set)  # Output: {1, 2}

# Using sets to remove duplicates from list
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = list(set(my_list))
print(unique_elements)  # Output: [1, 2, 3, 4, 5]
