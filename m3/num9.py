import numpy as np
from scipy.linalg import null_space

# Define the matrix A
A = np.array([[1, 0, -2], [0, 0, 0], [-3, 0, 6]])

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Sort the eigenvalues in increasing order
eigenvalues = np.sort(eigenvalues)

# Print the characteristic equation
print("The characteristic equation is (λ - {}) * (λ - {}) * (λ - {}) = 0".format(*eigenvalues))

# Print the eigenvalues
print("The eigenvalues are", eigenvalues)

# Calculate and print the bases for the eigenspaces
for i, eigenvalue in enumerate(eigenvalues):
    # Create a matrix B from A by subtracting the eigenvalue from the diagonal
    B = A - eigenvalue * np.eye(A.shape[0])
    
    # The null space of B is the eigenspace corresponding to this eigenvalue
    eigenspace = null_space(B)
    
    # Normalize the vectors in the eigenspace
    eigenspace = eigenspace / np.linalg.norm(eigenspace, axis=0)
    
    print("Basis for the eigenspace corresponding to eigenvalue {}:".format(eigenvalue))
    print(eigenspace)




# Find the characteristic equation, the eigenvalues, and the bases for the eigenspaces of the following matrix: 
    
# A = [[1, 0, -2], [0, 0, 0], [-3, 0, 6]]

# The characteristic equation is _______________ = 0

# Note: Enter the eigenvalues in increasing order.

# The eigenvalues are _______________
# Bases for the eigenspaces are _____

