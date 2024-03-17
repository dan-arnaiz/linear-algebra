import numpy as np

# Define a matrix
A = np.array([[4, -1], [2, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

# Diagonalization
# If A is diagonalizable, we can write it as A = PDP^-1 where D is a diagonal matrix
# containing the eigenvalues, and P is a matrix whose columns are the eigenvectors.
if len(eigenvalues) == A.shape[0]:
    P = eigenvectors
    D = np.diag(eigenvalues)
    A_reconstructed = P @ D @ np.linalg.inv(P)
    print("Diagonalization: A = PDP^-1:", A_reconstructed)

# Complex Vector Spaces
# Let's create a matrix that has complex eigenvalues
B = np.array([[0, -1], [1, 0]])
eigenvalues_B, eigenvectors_B = np.linalg.eig(B)

print("Complex Eigenvalues:", eigenvalues_B)
print("Complex Eigenvectors:", eigenvectors_B)