number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

total = number1 + number2

if(total < 101):
    print("Please recharge your account")
elif(total < 50 ):
    print("You can afford the trip")
else:
    print("Welcome back!")
