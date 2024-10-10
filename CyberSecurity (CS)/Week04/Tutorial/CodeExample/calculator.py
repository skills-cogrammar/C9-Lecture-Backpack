'''
Write a Python function calculator(operation, a, b) that takes three arguments:

- operation: a string that can be "add", "subtract", "multiply", or "divide".
- a: the first number (float or integer).
- b: the second number (float or integer).

The function should return the result of the appropriate arithmetic operation. For division, ensure that you handle division by zero by using error handling.

'''

# Create a function called calculator -> 3 (parameter)
def calculator(operation, a, b):
    # Open try ... except block
    try:
        # Check is the operator is add/subtract/multiply/divide
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b 
        elif operation == "divide":
            return a / b
        # If operator is not in choices, return Invalid Input
        else:
            return "Invalid Input"
    #If the user inserts 0 as b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
        

print(calculator("modulo", 10, 0))