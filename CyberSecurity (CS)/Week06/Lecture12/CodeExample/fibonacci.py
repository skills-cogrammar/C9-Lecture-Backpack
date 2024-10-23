'''
Fibonacci Sequence ?

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

'''

# Recursive approach of fibonacci
'''
Can you get the fibonacci(10)
Use recursion in python
'''

def fibonacci_recursive(n):
    # Base cases
    if n == 1 or n == 2:
        return 1
    # Recursive case
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_recursive(10))