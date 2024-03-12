import numpy as np
from scipy.linalg import null_space

# Define the matrix A
A = np.array([[1, -7], [0, 7]])

# Find the eigenvalues of A
eigenvalues = np.linalg.eigvals(A)

# For each eigenvalue, compute λI - A and find a basis for the null space
for λ in eigenvalues:
    λI_minus_A = λ * np.eye(A.shape[0]) - A
    basis = null_space(λI_minus_A)
    print(f"For eigenvalue λ = {λ}, a basis for the eigenspace is {basis}")
    print("The eigenvalue is:", λ)
    