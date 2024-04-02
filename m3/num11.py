import numpy as np

# Define the matrix A
A = np.array([[7, 0, 1], [2, 4, 2], [1, 0, 7]])

# Calculate the eigenvalues
eigenvalues = np.linalg.eigvals(A)

# Sort the eigenvalues from smallest to largest
eigenvalues = np.sort(eigenvalues)

print("The eigenvalues are", eigenvalues)

# Find the eigenvalues of A 
# A = [[7, 0, 1], [2, 4, 2], [1, 0, 7]]
# Enter the three eigenvalues. Enter the eigenvalues from smallest to largest. If eigenvalues are a multiple of zero of the characteristic equation then enter them repeatedly. eg. -1,2,2 or -3,-3,1.