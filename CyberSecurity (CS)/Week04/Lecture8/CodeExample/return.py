'''
Return values in python function

Parameters: What the function expects
Arguments: Actual values passed to the function
'''


# def add(x, y): #Function parameters
#     result = x + y
#     print(result)
#     return result


# total_sum = add(10, 20)  #Function arguments #Output: 30

# print(total_sum)

score = 60

def determine(points):
    if points < 50:
        print("Hello World")
        return "The student has failed."
    elif points > 50:
        print("Hello World")

        return "The student has passed"
    

result = determine(score)
print(result)