import pdb
import logging


def add_numbers(a, b):
    print("a: ", a)
    logging.debug("debugging something")
    print("b: ", b)
    result = a + b
    print("result: ", result)
    return result


# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))

# add_numbers(a, b)


# inbuilt python debugger


def multiply(a, b):
    # pdb.set_trace()
    breakpoint()  # automatically calls pdb.set_trace()
    return a * b


print(multiply(2, "5"))  # intentional error for debugging

# print("Python" * 10)
