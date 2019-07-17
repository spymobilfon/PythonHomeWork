# Set matrix
matrix = [[3, 5, 7],
          [2, 6, 8],
          [6, 9, 0],
          [12, 25, 41]]

# Print row in matrix
print("Строки матрицы:")
for row in matrix:
    print(row)

# Print column in matrix
print("Столбцы матрицы:")
print([element[0] for element in matrix])
print([element[1] for element in matrix])
print([element[2] for element in matrix])