import numpy as np

def matrix_operations(operation, matrix1, matrix2=None):
    if operation == 'create':
        return np.array(matrix1)
    elif operation == 'add':
        return np.add(matrix1, matrix2)
    elif operation == 'subtract':
        return np.subtract(matrix1, matrix2)
    elif operation == 'multiply':
        return np.dot(matrix1, matrix2)
    else:
        return "Invalid operation"

# Create matrices
matrix1 = matrix_operations('create', [[3, -1], [-2, 2]])
matrix2 = matrix_operations('create', [[2, 0], [1, 4]])

# Add matrices
print("Addition")
print(matrix_operations('add', matrix1, matrix2))

# Subtract matrices
print("Subtraction")
print(matrix_operations('subtract', matrix1, matrix2))

# Multiply matrices
print("Multiplication")
print(matrix_operations('multiply', matrix1, matrix2))

# Invert matrix
# print("Inversion")
# print(matrix_operations('invert', matrix1))