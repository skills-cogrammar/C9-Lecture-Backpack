# LISTS
# names = ["John", "Jane", "Mary", "Moses", "Moses"]
# members = list()
# print(members.append("Hello World"))
# # print(names.append("Lisa"))
# # ["John", "Jane", "Mary", "Moses", "Lisa"]
# # print(names.pop())
# # # ["John", "Jane", "Mary", "Moses"]

# # Slicing method
# print(names[::-1])


# SETS
# names_set = {"Jane", "John", "Mary"}
# name_set2 = {"Lisa", "Sally", "Dan", "Mary"}

# my_set = set()

# print(names_set)
# names_set.pop()
# print(names_set)

# union_set = names_set.union(name_set2)
# print(union_set)

# intersection = names_set.intersection(name_set2)
# print(intersection)


# TUPLES
# my_tuple = ("James", "John", "Mary", "Walobwa")
# print(my_tuple[2])
# print(my_tuple[1:])

# name1, name2, name3, name4 = my_tuple

# print(name4)

my_list = [10, 0, "Jane", [50, "Mary", ["John", "Jones"], ["Ericka", "Bob"]], ["Dan", "Walobwa"]]
name_wanted = my_list[3][3][1]
name_wanted = my_list[4][0]

print(name_wanted)
# Bob
# Dan

# Tuples can be nested inside sets
my_tuple = (1,2,[3,4])
my_tuple[0] = 99
print(my_tuple)