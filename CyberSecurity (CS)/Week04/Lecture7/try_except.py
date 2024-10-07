# Version 1
num1 = input("Num 1: ")
num2 = input("Num 2: ") 

print(f"{num1 / num2 = }")


# Version 2
num1 = input("Num 1: ")
num2 = input("Num 2: ")

try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print("Please make sure you only enter numbers!")


print(f"{num1 / num2 = }")


# Version 3
num1 = input("Num 1: ")
num2 = input("Num 2: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    print(f"{num1 / num2 = }")
except ValueError:
    print("Please make sure you only enter numbers!")
except ZeroDivisionError:
    print("Cannot devide by Zero!")


# Version 4
num1 = input("Num 1: ")
num2 = input("Num 2: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    print(f"{num1 / num2 = }")
except ValueError:
    print("Please make sure you only enter numbers!")
except ZeroDivisionError:
    print("Cannot devide by Zero!")
finally:
    print("Thank you for using the division program!")


# Version 5
num1 = input("Num 1: ")
num2 = input("Num 2: ")

try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print("Please make sure you only enter numbers!")
except ZeroDivisionError:
    print("Cannot devide by Zero!")
else:
    print(f"{num1 / num2 = }")
finally:
    print("Thank you for using the division program!")


# Student challenge
# Print the first letter of a given word
# Fix using try..except
word = input("Please enter any word: ")
print(word[0])


# Conditions
num1 = input("Num 1: ")
num2 = input("Num 2: ")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    if num2 != 0:
        print(f"{num1 / num2 = }")
    else:
        print("Cannot devide by Zero!")
else:
    print("Please make sure you only enter numbers!")

# Student challenge
# Print the first letter of a given word
# Fix using conditions
word = input("Please enter any word: ")
print(word[0])