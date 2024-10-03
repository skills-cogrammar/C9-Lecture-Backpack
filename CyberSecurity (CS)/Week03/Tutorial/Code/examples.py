# Guessing game
from random import randint

number = randint(0, 100)


while True:

    guess = int(input("Guess a number between 1 and 100: "))

    if guess > number:
        print("You might want to guess lower.")
    elif guess < number:
        print("You might want to guess higher.")
    else:
        print(f"You got it! The number is {number}")
        break
# How can we change the condition to give the user a set amount of guesses


# Mulitpication table
number = int(input("For which number would you like to see a multiplication table: "))

for i in range(1, 13):
    print(f"{number} x {i} = {number*i}")
# How can we change the program to allow a user to choose up to which number we multiply?


# Voting system
VOTE_MENU = """Please select a team to vote for:

A - Team 1
B - Team 2
C - Team 3
D - Team 4
: """

votes = int(input("Please enter the amount of voter allowed: "))
team1 = 0
team2 = 0
team3 = 0
team4 = 0

while votes > 0:
    user_vote = input(VOTE_MENU)

    if user_vote == "A":
        team1 += 1
    elif user_vote == "B":
        team2 += 1
    elif user_vote == "C":
        team3 += 1
    elif user_vote == "D":
        team4 += 1
    # Why do we use elif instead of just if-statements?

if team1 > team2 and team1 > team3 and team1 > team4:
    print("Team 1 has won!")
if team2 > team1 and team2 > team3 and team2 > team4:
    print("Team 2 has won!")
if team3 > team1 and team3 > team2 and team3 > team4:
    print("Team 3 has won!")
if team4 > team1 and team4 > team2 and team4 > team3:
    print("Team 4 has won!")
# Is there a better way we can store the votes for our teams?


# Password Checker
# one uppercase letter, one lowercase letter, and one digit
upper = False
lower = False
digit = False

while True:
    user_password = input("Please enter a password: ")

    for char in user_password:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper = True
        if char in "abcdefghijklmnopqrstuvwxyz":
            lower = True
        if char.isnumeric():
            digit = True

    message = ""
    if upper and lower and digit:
        message += "Thank you for entering a password!"
        break
    if not upper:
        message += "Missing uppercase character\n"
    if not lower:
        message += "Missing lowercase character\n"
    if not digit:
        message += "Missing digit"

print(message)
    

