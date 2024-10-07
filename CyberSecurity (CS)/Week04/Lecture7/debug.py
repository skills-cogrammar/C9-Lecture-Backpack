LINE = "-"*80
WELCOME = "Welcome to Word Edit"
MENU_TEXT = """Select an option below:
1. Remove Character
2. Add New Character
3. Enter New Word

0. Quit
"""

print("{0}\n{1}\n{0}".format(LINE, WELCOME))
user_word = input("Please enter the word you would like to edit: ")


while True:
    print("{0}\nYour word is: {1}\n{0}".format(LINE, user_word))
    menu = input(MENU_TEXT) # Change to int or change conditions to strings
    if menu == 1:
        remove_char = input("Enter the character you would like to remove: ")
        if remove_char in user_word:
            print(user_word.replace(remove_char, "")) # Replace is not saved
        else:
            print("Character does not exist in user word.")
    elif menu == 2:
        new_char = input("Enter the character you would like to add: ")
        print("Please choose an index for the character: ")
        print(user_word)
        for i in range(len(user_word)):
            print(i, end="")
        print()
        user_index = input() # Change to int show students type()
        user_word = user_word[:user_index] + new_char + user_word[user_index:]
    elif menu == 3:
        # new word stored in new variable not overriding original word
        new_word = input("Please enter the new word you would like to edit:")
        print("Word changed to: {}".format(new_word))
    else:
        print("Goodbye")
        break
    


