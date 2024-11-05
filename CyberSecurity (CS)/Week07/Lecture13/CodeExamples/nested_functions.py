age = 10 #global variable

def voter():
    age = 34
    def greet():
        nonlocal age
        print(age)
    greet()

voter()

fruit = input("Enter a fruit: ")

fruits = ["apple", "mango", "banana"]

fruits.append(fruit)
print(fruits)
print(len(fruits))
