import os


# Defining the ls function.
def ls(path="."):
    for file in os.listdir(path):
        print(file)


# Calling the ls function
ls()
