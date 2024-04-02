import numpy as np

# Define the matrix A
A = np.array([[-1, -4], [5, 7]])

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Sort the eigenvalues and eigenvectors by the eigenvalues
idx = eigenvalues.argsort()[::-1]   
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:,idx]

print("The eigenvalues are:")
print(eigenvalues)

print("The corresponding eigenvectors are:")
print(eigenvectors)




# Find the eigenvalues and bases for the eigenspaces of A. 

# A = [[-1, -4], [5, 7]]
# Enter the eigenvalues in order of size (bigger real part first, or bigger imaginary part first if real parts are equal).

# lambda1 = _____

# lambda2 = _____

# Which of the following are valid bases for the eigenbases of lambda1 and lambda2? 