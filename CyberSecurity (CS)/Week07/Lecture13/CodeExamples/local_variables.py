"""
local variables -> defined within a function and only accessible within that function
- once a funtion completes execution, the local variable is removed from memory
"""

def voter():
    age = 23 # local varibale
    print(age)

voter()
