import sys

def wc(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_counter = len(lines)
        word_counter = sum(len(line.split()) for line in lines)
        char_counter = sum(len(char) for char in lines)

        print(f"{line_counter} {word_counter} {char_counter}")

wc(sys.argv[1])
