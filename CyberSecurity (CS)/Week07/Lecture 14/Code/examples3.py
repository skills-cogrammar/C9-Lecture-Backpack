def calculate_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

def calculate_median(numbers):
    numbers.sort()
    mid_index = len(numbers) // 2
    if len(numbers) % 2 == 0:  # even number of elements
        median = (numbers[mid_index] + numbers[mid_index + 1]) / 2
    else:
        median = numbers[mid_index]
    return median

# Main function
def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in user_input.split(",")]
    
    average = calculate_average(numbers)
    print(f"The average is: {average}")
    
    median = calculate_median(numbers)
    print(f"The median is: {median}")

main()
"""
Incorrect input delimiter: The code prompts for input separated by spaces but splits by commas.
Index error in median calculation: For even-length lists, the code uses the wrong indices for calculating the median.
Division by zero error: No check is included to handle the case where the list is empty, which would cause a division error in calculate_average.
"""