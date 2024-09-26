random_word = input("Please enter a random word: ")
word_len = len(random_word)
last_letter = random_word[-1]
new_word = random_word.replace(last_letter, '$')
print(new_word[0])
