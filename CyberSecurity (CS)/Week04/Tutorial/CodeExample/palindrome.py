'''
MALAYALAM

Write a function is_palindrome(s) that checks if a given string is a palindrome (reads the same forwards and backwards). Return True if it is, otherwise return False.

Submit your solution in the Questions Tab.
'''


word = input("Enter a word or a sentence: ")

# Create a function called is_palindrome(string)
def is_palindrome(s):

    try:

        clean_string = ""

        for char in s:
            if char.isalnum():
                clean_string += char.lower()

        # Reverse the initial string
        s_reverse = clean_string[::-1]

        # Check if the initial string is equal to the reversed string
        if (clean_string == s_reverse):
            return True
        else:
            return False
    except TypeError:
        return "Please insert strings"

print(is_palindrome(word))

'wiped'

# A man, a Plan, a canal, Panama!


