"""
global varibale -> defined outside of any function and accessible throughout the entire file/module in which it is declared
"""
age = int(input("Please enter your age: ")) #global variable

def voter():
    global age
    age = 34
    print(age)

voter()
print(age)
