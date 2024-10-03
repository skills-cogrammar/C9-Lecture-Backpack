#For loop
#for item in sequence


# #For each character/letter in name
# for character in name:
#     #check if the letter/character e is in name
#     if character == 'e':
#         #print the character
#         print(character)
#     else:
#         print("Character not found")


# name = 'Hyperion'
# for index, character in enumerate(name):
#     if character == 'e':
#         print(f"Character: {character}, Position: {index}")


'''
Write a program that prints out the position of character e
'''
# for i in range(0, len(name)):
#     print(name[i])


# for i in range(0, len(name)):
#     if name[i] == 'e':
#         print(f'Character {name[i]}, is at position {i}')

# name = "Hyperion"

# for i in range(0, len(name)):
#     print(f"Character at index {i}: {name[i]}")



# print(name[3])

#for each number from 0 to 5
# for i in range(5):
#     #if the count is 3
#     if i == 3:
#         #stop the loop
#         break #Ends the code if condition is met
#     print(i)


# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

total_sum = 0
# Loop through numbers from 1 to 100
for number in range(1, 101):
# Check if the current number is divisible by 3
    if number % 3 == 0:
        total_sum += number # Add the number to the sum if the condition is met

print(total_sum)