
matrix = [[1, 2, 3],  #1, 4, 7
          [4, 5, 6],  #2, 5, 8
          [7, 8, 9]]  #3, 6, 9

transpose_matrix = []

for col in range(len(matrix)):
    transpose_matrix.append([])
    for row in range(len(matrix)):
        print(transpose_matrix)
        transpose_matrix[col].append(matrix[row][col])

print(transpose_matrix)
