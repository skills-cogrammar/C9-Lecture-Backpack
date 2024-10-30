# Example 1
def get_average(x, y ,z):
    average = x + y + z /3
    return average

print(get_average(3, 5, 7)) # Ouput should be 5 but we get 10.33333

# We can form a hypothesis that the calculation is incorrect.
# One approach we can take is to calculate the total before we devide
def get_average(x, y ,z):
    total = x + y + z
    average = total/3
    return average

# Example 2
def times_ten(value):
    return value * 10

value = input("Please enter a value to multiply by 10: ")
print(times_ten(value))

# Example 3
def calculate_area(radius):
    pi = 3.14159
    area = p * (radius ** 2)  # p is not defined
    return area

print(calculate_area(5))  # Expected: 78.53975


# Example 4
def count_to_five():
    i = 1
    while i <= 5:
        print(i)
        # i += 1 is missing, causing an infinite loop

count_to_five()

