# Strings

my_str = "Hello world!"

my_str = input("Please enter a sentence: ")# input produces string result

# remove all spaces from string
print(my_str.replace(" ", ""))
print(my_str)# Notice that my_str stays the same after replace() call
# Does anyone know how I can control how many occurences of the charater should be removed?

# Slicing first 5 characters
print(my_str[0:5])

# Slicing first 5 characters reverse
print(my_str[5:0:-1]) # remember it goes up to including
print(my_str[5::-1])

# Concatenation
print(my_str[0:3] + my_str[5:8])
# Ask student if they know of diffirent ways to concatenate before showing 
# f-string and format()
print(f"{my_str[0:3]}{my_str[5:8]}")
print("{}{}".format(my_str[0:3], my_str[5:8]))



# Numbers
num1 = 5
num2 = 18

result = num1 + num2
print(result)

# Ask students what is wrong with the following code.
num1 = input("Please enter a number: ")
num2 = input("Please enter another number: ")

result = num1 + num2
print(result)

# Once the code is fixed ask the student what other operators there are for numbers
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

result = num1 + num2
result1 = num1 - num2
result2 = num1 * num2
result3 = num1 / num2
result4 = num1 % num2
result5 = num1 // num2

print(result)


# Conditional Statements
# Calculate the grade average of a student and provide a grade symbol
# 90-100 : A
# 80-89 : B
# 70-79 : C
# 60-69 : D
# 50-59 : E

grade1 = 57
grade2 = 77
grade3 = 75

grade_avg = grade1 + grade2 + grade3

# Ask students to suggest conditions
if grade_avg >= 90:
    print("Grade: A")
elif grade_avg >= 80:
    print("Grade: B")
elif grade_avg >= 70:
    print("Grade: C")
elif grade_avg >= 60:
    print("Grade: D")
elif grade_avg >= 50:
    print("Grade: E")

# Can also be set up like this
if 90 <= grade_avg <= 100:
    print("Grade: A")
elif 80 <= grade_avg <= 89:
    print("Grade: B")
elif 70 <= grade_avg <= 79:
    print("Grade: C")
elif 60 <= grade_avg <= 69:
    print("Grade: D")
elif 50 <= grade_avg <= 59:
    print("Grade: E")
# Conditions range not dependant on other conditions