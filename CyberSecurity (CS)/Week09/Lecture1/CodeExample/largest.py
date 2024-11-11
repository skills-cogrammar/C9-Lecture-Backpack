'''
Find the larget number in a matrix
'''

# Solution 1
matrix = [
[3, 5, 7],
[1, 9, 4],
[8, 2, 6]
]
max_value = matrix[0][0]

for row in matrix:
    for value in row:
        if value > max_value:
            max_value = value

print(f"The maximum value in the matrix is: {max_value}")



# Solution 2
matrix = [
[3,5,7],
[1,9,4],
[8,2,6]
]
max = float('-inf')

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] > max:
            max = matrix[i][j]

print(max)