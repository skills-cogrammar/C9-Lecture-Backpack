age = int(input("Please enter your age: "))

if (age > 0 and age < 18):
    print("You're not eligible to vote.")
elif(age <= 0 or age > 130):
    print("Invalid age")
else:
    print("You can vote")
