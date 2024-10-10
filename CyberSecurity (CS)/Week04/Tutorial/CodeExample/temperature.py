'''
Write a Python function that converts a temperature from Celsius to Fahrenheit and handles input errors.

- Take a single parameter, celsius, which represents the temperature in Celsius.
- Use a try-except block to:
    - Catch and handle TypeError if the input is not a number, returning "Invalid input. Please enter a number."

(celsius * (9/5)) + 32
'''

def celcius_to_fh(celcius):
    try:
        #32.0
        celcius_float = float(celcius)

        fahrenheit = (celcius_float * (9/5)) + 32
        return fahrenheit
    except TypeError:
        return "Invalid input. Please enter a number."