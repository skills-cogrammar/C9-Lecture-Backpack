def factorial(n):
    result = 1
    if n > 0:
        for i in range(1, n + 1):
            result = result * i
    
    return result

# 10
# 10 * 9 * 8 ...1
# 5 * 4 * 3 * 2 * 1

print(factorial(5))


def factorial_recursive(n):
    # Base case
    if n < 1:
        return n
    
    # Recursive approach
    return n * factorial(n-1)


print(factorial_recursive(5))
