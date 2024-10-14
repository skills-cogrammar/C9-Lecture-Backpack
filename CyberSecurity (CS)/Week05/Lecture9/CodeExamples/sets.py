'''
SETS
'''

# Does not allow duplicates

# Cannot perform indexing (Unordered)
# result = my_set[0]

# # Converting a list to a set
# my_list = [ "Bonaventure", "Dan", "Armand", "Dan"]
# converted_list = set(my_list)
# print(converted_list)



# Add
my_set = { 1, 2, 3, 4, 5 }
my_set2 = { 2, 6, 7, 8, 9, 10 }

my_set.add(10)
print(my_set)

# Remove
my_set.remove(3)
print(my_set)

# Union
combined_set = my_set.union(my_set2)
print(combined_set)

# Intersection
intersection = my_set.intersection(my_set2)

print(intersection)