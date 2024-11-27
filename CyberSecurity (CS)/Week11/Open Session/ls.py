import os

def ls(path="."):
    for file in os.listdir(path):
        print(file)


ls()
