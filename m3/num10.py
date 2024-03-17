import numpy as np

# Define the eigenvalues and eigenvectors
eigenvalues = np.array([0, 16, -16])
eigenvectors = np.array([[0, 1, -1], [1, -1, 1], [0, 1, 1]])

# Create a diagonal matrix with the eigenvalues
D = np.diag(eigenvalues)

# Calculate the matrix A
A = eigenvectors @ D @ np.linalg.inv(eigenvectors)

print("The matrix A is:")
print(A)





# Find a 3x3 matrix A that has eigenvalues λ = 0, 16, -16 with corresponding eigenvectors
# [0, 1, -1], [1, -1, 1], [0, 1, 1].

# Write answer respectively