'''
Recursion
'''

# Recursive
def walk_recursive(steps):
    # Base case
    if steps == 0:
        return 1
    # Recursive function
    print(steps)
    walk_recursive(steps - 1)

walk_recursive(1000)


'''
TO DO:
1. Place the print statement below the recursive function
2. Place the print statement above the recursive function

Observe the output.
'''


# Iterative approach
# While loop
def walk(steps):
    while steps > 0:
        print(steps)
        steps -= 1


# For loop
def walk1(steps):
    if steps > 0:
        for i in range(1, steps + 1):
            print(i)


walk1(100000)