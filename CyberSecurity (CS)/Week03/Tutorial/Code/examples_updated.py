# Guessing game

from random import randint

number = randint(0, 100)

# # Tell user if guess is:
# # Too high
# # Too low
# # Correct
while True:
    guess = int(input("Please enter a number: "))

    if guess > number:
        print("Your guess is too high!")
    elif guess < number:
        print("Your guess is too low!")
    elif guess == number:
        print(f"Correct guess number is {number}")
        break


# Multiplication Table
number = int(input('Enter a number to multiply: '))

for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")







# # Voting system
VOTE_MENU = """Please select a team to vote for:

A - Team 1
B - Team 2
C - Team 3
D - Team 4
: """

votes = int(input("Please enter the amount of voters: "))
team1 = 0
team2 = 0
team3 = 0
team4 = 0

while votes > 0:

    user_vote = input(VOTE_MENU)

    if user_vote.lower() == 'a':
        team1 += 1
    elif user_vote.lower() == 'b':
        team2 += 1
    elif user_vote.lower() == 'c':
        team3 += 1
    elif user_vote.lower() == 'd':
        team4 += 1
    votes -= 1

if team1 > team2 and team1 > team3 and team1 > team4:
    print("Team 1 has won!")
elif team2 > team1 and team2 > team3 and team2 > team4:
    print("Team 2 has won!")
elif team3 > team1 and team3 > team2 and team3 > team4:
    print("Team 3 has won!")
elif team4 > team1 and team4 > team2 and team4 > team3:
    print("Team 4 has won!")


# Password checker
# one uppercase, one lowercase, one digit
upper = False
lower = False
digit = False

while not upper and not lower and not digit:
    user_password = input("Please enter a password: ")

    for char in user_password:
        if not upper and char in "ABCDEFGHIJKLMNOPQRSTUVXYZ":
            upper = True
        elif char in "abcdefghijklmnopqrstuvxyz":
            lower = True
        elif char in "0123456789":
            digit = True

    message = ""
    if upper and lower and digit:
        message += "Thank you for entering a password!"
    if not upper:
        message += "Missing uppercase letter\n"
    if not lower:
        message += "Missing lowercase letter\n"
    if not digit:
        message += "Missing digit\n"
    print(message)