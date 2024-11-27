import sys


def wc(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # List Comprehension
        # words = []
        # for line in lines:
        #     words.append(len(line.split()))
        # word_counter = sum(words)

        line_counter = f'Number of lines: {len(lines)}'
        word_counter = f'Number of words: {sum(len(line.split()) for line in lines)}'
        char_counter = f'Number of characters: {sum(len(char) for char in lines)}'

        print(f"{line_counter}\n{word_counter}\n{char_counter}")


file_path = sys.argv[1]
wc(file_path)
