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

print(invert_matrix(matrix_2x2))
print(invert_matrix(matrix_3x3))
print(invert_matrix(matrix_4x4))