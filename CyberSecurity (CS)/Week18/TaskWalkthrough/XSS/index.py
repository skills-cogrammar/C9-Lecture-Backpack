
def something_malicious():
    print("Something Malicious")

with open("malicious.txt", mode="r") as user_input:
    value = user_input.read()



def calculator(expression):
    num1, operand, num2 = expression.split(" ")

    if (operand == "+"):
        print(int(num1) + int(num2))


calculator("1 + 2")
# File handling
# Accept user input