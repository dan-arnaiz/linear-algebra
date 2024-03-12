import numpy as np

A = np.array([[-4, 0, 1], [-4, 1, -4], [1, 0, -4]])
x = np.array([5, 10, 5])

# Multiply A by x
Ax = np.dot(A, x)

# Divide Ax by x to get a vector where all elements should be equal to the eigenvalue
lambda_vector = Ax / x

# Check if all elements in lambda_vector are the same (within a small tolerance due to potential floating point errors)
if np.allclose(lambda_vector, lambda_vector[0]):
    print("x is an eigenvector of A with eigenvalue λ =", lambda_vector[0])
else:
    print("x is not an eigenvector of A")