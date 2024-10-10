'''
Write a function safe_divide(a, b) that takes two numbers and returns their division. If division by zero is attempted, handle the error and return a message like "Division by zero is not allowed."
'''

# Create a function called safe_divide that takes in 2 parameters (numbers)
def safe_divide(a, b): # Function name/declaration
    # Divides and returns numbers a and b
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except TypeError:
        return "An integer is required."

print(safe_divide(10, 0))