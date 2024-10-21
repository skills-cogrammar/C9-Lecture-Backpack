# Input and Output
name = input("Please enter a name: ")

print("Hello World!")


# Opening Files

my_file = open("my_file.txt", "r")
# Delete text file to show file not found error.

# Creating a new file when opening a file in write that does not exist
new_file = open("new_file.txt", "w")

# Closing files to prevent memory leaks
my_file.close()
new_file.close()

# Using "with" to open files
with open("my_file.txt", 'r') as my_file:
    # Work with file inside block
    pass



# Reading from files
file = open("paragraph.txt", "r")

# Read all data as single string
text = file.read()
print(text)

# Read one line at a time
one_line = file.readline()
print(one_line)

# Get all lines of file in a list.
lines = file.readlines()
print(lines)

for line in lines:
    print(line)

# Leave the close out and ask students if they can see something wrong.
file.close()

# Read the data from users.txt and print the data to the terminal in a user-friendly manner.
with open("users.txt", "r") as user_file:
    user_file.readline()
    for line in user_file.readlines():
        line = line.strip().split(",")
        line = " ".join(line)
        print(line)


# Writing to files
new_file = open("my_file.txt", "w")

names = ["James", "Tina", "Martha", "David"]

for name in names:
    new_file.write(name + "\n") # Show first without new line

new_file.writelines(names)

# Create a program that will write 1-10 in a text file. Each number on a new line.
with open("numbers.txt", "w") as number_file:
    for i in range(1, 11):
        number_file.write(f"{i}\n")


# Appending Data
with open("dogs.txt", "a") as dogs_file:
    dogs_file.write("Boxer")
# Inform students to look at the file and if it ends with a new line or a value.
    


# Write a program that will take the names from one file and the ages from another
# combine them and write them to a 3rd text file.
name_file = open("names.txt", "r")
age_file = open("ages.txt", "r")

names = name_file.readlines()
ages = age_file.readlines()

name_file.close()
age_file.close()

names_and_ages = ""
for i in range(len(names)):
    names_and_ages += names[i].replace("\n", ",") + ages[i]

# Using zip()
for name, age in zip(names, ages):
    names_and_ages += name.replace("\n", ",") + age

new_file = open("names_and_ages.txt", "w")
new_file.write(names_and_ages)
new_file.close()
