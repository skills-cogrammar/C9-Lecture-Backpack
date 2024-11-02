'''
Functions in python
'''

def addition1():
    """
    Function body: the step by step
    guidance on what the function does.
    Return: breaks the function and returns a value as instructed
    """
    x = 10
    y = 20
    return x + y

addition1() # Function call


def addition2(num1, num2):
    """
    Function Parameters: What the function expects
    Function arguments: Actual data/values passed to functions
    """
    return num1 + num2


x = 10
y = 20
addition2(x, y)


"""
SCOPES
Local scopes: Variables declared within a block
Global scopes: Variables that can be accessed throughout the file (globally)
"""

def addition3():
    """
    Variables x and y are locally scoped
    """
    x = 10
    y = 20

    results = x + y
    return results


print(x)
print(y)

for i in range(0, 10):
    """
    Count variable is locally scoped
    """
    count = 0


# Variables x and y are in the global scope
x = 10
y = 20

def addition4():
    result = x + y
    return result

print(x)


# Using the global keyword
def addition5():
    global x
    x = 10
    y = 20
    return x + y

addition5()
print(x)




# Closures
def outer_function(x):

    def inner_function(y):
        return x + y
    return inner_function

result = outer_function(5)
result2 = outer_function(10)



print(result(10))


def values():
    area = 10 * 20
    parameter = (10 + 20) * 2
    return area, parameter

print(values())


# Enumerate
my_list = [10, 20, 30, 40]

for i in range(0, len(my_list)):
    print(my_list[i])


for i, number in enumerate(my_list, start=0):
    print(i, number)



def addition():
    return 10 + 20

addition()
