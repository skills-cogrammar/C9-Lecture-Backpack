'''
2D Lists
'''

# Manual way
family_matrix = [
["John", "x", "Mary", "Jane"],
["Dan", "Armand", "Bonaventure", "Zahra"],
["Adil", "Jones", "Amel", "Laima"],
["x", "Jerome", "Sarah", "Robert"]
]

# Accessing
print(family_matrix[2][1])
print(family_matrix[1][2])

# Looping over a matrix
for row in family_matrix:
    print(row)
    for person in row:
        print(person)


# Using indices and nested for loops
for i in range(len(family_matrix)):
    for j in range(len(family_matrix)):
        print(family_matrix[i][j])








# Using loops
side_rows = 4
seat_columns = 3


# Parent list
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


for i in range(side_rows):
    row = []
    for j in range(seat_columns):
        row.append(0)
    matrix.append(row)

print(matrix)