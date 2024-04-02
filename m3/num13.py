import numpy as np

# Define the matrix A
A = np.array([[5, -2], [1, 3]])

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# The matrix P is the matrix of eigenvectors
P = eigenvectors

# The matrix C is a rotation matrix with the real and imaginary parts of the first eigenvalue
a, b = eigenvalues[0].real, eigenvalues[0].imag
C = np.array([[a, -b], [b, a]])

print("The matrix P is:")
print(P)

print("The matrix C is:")
print(C)



# Find an invertible matrix P and a matrix C of form [[a, -b], [b, a]] such that A = PCP^-1

# A = [[5, -2], [1, 3]]

# P = ?
# C = ?