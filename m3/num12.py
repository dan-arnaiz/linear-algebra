import numpy as np

# Define the matrix A
A = np.array([[9, 0, 0], [0, 8, 0], [0, 4, 8]])

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Calculate the algebraic and geometric multiplicities
algebraic_multiplicities = np.bincount(eigenvalues.astype(int))
geometric_multiplicities = [np.linalg.matrix_rank(eigenvectors[:, eigenvalues == eigenvalue]) for eigenvalue in np.unique(eigenvalues)]

# Check if the matrix is diagonalizable
is_diagonalizable = all(geo_mult == alg_mult for geo_mult, alg_mult in zip(geometric_multiplicities, algebraic_multiplicities))

print("The matrix is", "diagonalizable" if is_diagonalizable else "not diagonalizable")



# Use a method to determine whether the matrix is diagonalizable.
# A = [[9, 0, 0], [0, 8, 0], [0, 4, 8]
