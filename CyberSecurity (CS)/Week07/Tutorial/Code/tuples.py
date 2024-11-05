str_tuple = ["This", "is", "a", "list", "of", "strings"]
int_tuple = [1, 2, 3, 4, 5]
float_tuple = [1.2, 2.4, 3.0, 2.5, 2.1]
mixed_tuple = [1, "Hello", True, 3.4]

# Ask student ot create a tuple that contains the details of someone.
# e.g. details = ('name', 'surname', 'age', 'address')

numbers = (1,4,5,3,6,4,6,7,5,4,4,6,5,7)
print(numbers.count(4))

details = ('name', 'surname', 'age', 'address')

details.index('age')

for data in details:
    print(data)

for i in range(len(details)):
    print(details[i])