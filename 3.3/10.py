import numpy as np

# Define the matrix
A = np.array([[6, 0, 0], [-7, 13, 0], [1, 5, 2]])

# The eigenvalues are the diagonal elements of the matrix
eigenvalues = np.diag(A)

# Sort the eigenvalues in increasing order
eigenvalues_sorted = np.sort(eigenvalues)

print("Eigenvalues in increasing order: ", eigenvalues_sorted)