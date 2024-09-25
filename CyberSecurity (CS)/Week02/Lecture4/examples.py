# Creating boolean values
my_bool = True
my_bool2 = False

print(my_bool)
print(my_bool2)

# Creation of IF-statement
if True:
    print("True")

my_bool = True
if my_bool:
    print("True")

# Integer Conditions
if 29 < 30:
    print("29 is smaller than 30")

my_condition = 30 != 15
if my_condition:
    print("The condition is true!")

# String Conditions
if "Hello" == "Hello":
    print("Same stings!")

my_string = "Goodbye"
if my_string.lower() == "goodbye":
    print("Bye bye!")

# Create an IF-statment that determines if a string is larger than 5 characters.
# (Student Challenge) HINT: LEN()
my_string = "Hello world!"
if len(my_string) > 5:
    print("This word has more than 5 characters.")

# Using "and" and "or"
result = 5 + 17
if result > 10 and result < 100:
    print("Result falls in the range 10-100.")

num = 10
if num < 15 or num > 25:
    print("Number fall ouside of the range 15-25")

# Create an if-statement that determines if a value is larger than 10 and is an even number.
# (Student Challenge)
num = 30
if num > 10 and num%2 == 0:
    print(f"{num} is even and larger than 10.")

# ELIF
num = 19

if num < 10:
    print(f"{num} is smaller than 10!")
elif num < 20: # Change elif to if to show how it executes differently.
    print(f"{num} is smaller than 20!")

# Menu example
MENU = """Please select an option below:
1. Option 1
2. Option 2
3. Option 3
: """
user_choice = input(MENU)
if user_choice == "1":
    print("Option 1 selected!")
elif user_choice == "2":
    print("Option 2 selected!")
elif user_choice == "3":
    print("Option 3 selected!")

# Create a if-elif statement to determine the grade of a student (Student Challenge)
# Score - Grade
# 90-100 - A
# 80-89 - B
# 70-79 - C
# 60-69 - D
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")


# ELSE
number = 10
if number > 10:
    print("The number is greater than 10.")
elif number == 10:
    print("The number is exactly 10.")
else:
    print("The number is less than 10.")

# We can incorperate an else in our MENU to show the user they haven't selected anything
user_choice = input(MENU)
if user_choice == "1":
    print("Option 1 selected!")
elif user_choice == "2":
    print("Option 2 selected!")
elif user_choice == "3":
    print("Option 3 selected!")
else: # Remove else and add "no option" print below if-statement to show behaviour changes.
    print("No option selected!")

# Write an if statement that will determine the correct age group of a user. (Student Challenge)
# 0-13 - Child
# 14-18 - Teenager
# 19-60 - Adult
# 60+ - Senior
age = 25

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Login example
username = "admin"
password = "password123"

if username == "admin" and password == "password123":
    print("Login successful!")
elif username == "admin":
    print("Incorrect password.")
else:
    print("User not found.")


# Create an if statement that will determine if a user entered a valid email address
# Check that the email contains an '@' and a '.'
email = "peter@pan.com"
if '@' in email and '.' in email:
    print("Email Valid!")
