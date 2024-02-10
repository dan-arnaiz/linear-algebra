import numpy as np

def invert_matrix(matrix):
    determinant = np.linalg.det(matrix)
    print(f"Determinant: {determinant}")
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return "This matrix is not invertible"

# testcases
matrix_2x2 = [[4, 7], [2, 6]]
matrix_3x3 = [[4, 7, 2], [2, 6, 1], [1, 2, 3]]
matrix_4x4 = [[4, 7, 2, 1], [2, 6, 1, 1], [1, 2, 3, 1], [1, 1, 1, 1]]
matrixex1 = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
test_5x5 = [[1, 3, -3, 3, -3], [2, 7, 0, -2, -4], [0, 0, 1, 0, 5], [0, 0, 2, 1, 2], [0, 0, 0, 3, -5]]


print(invert_matrix(matrix_2x2))
print(invert_matrix(matrix_3x3))
print(invert_matrix(matrix_4x4))
print(invert_matrix(matrixex1))
print(invert_matrix(test_5x5))



def scalar_multiply(matrix, scalars):
    return [[row[i]*scalars[i] for i in range(len(row))] for row in matrix]

matrix = [[4, 7, 2], [2, 6, 1], [1, 2, 3]]
scalars = [-2, -3, 3]
result = scalar_multiply(matrix, scalars)
print(result)