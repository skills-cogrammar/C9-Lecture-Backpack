age = 2
password_correct = False
money = 100

if age > 18:
    if password_correct == True and money > 100:
        print("You may withdraw the money")
elif age > 18 and password_correct == False:
    print("Please use the correct pasword.")
elif age < 18 and password_correct == True:
    print("You're not allowed access due to age limit.")
else:
    print("Incorrect Details")

# for i in range(100):
#     print(i)
