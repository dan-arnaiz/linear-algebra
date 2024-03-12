import numpy as np

# Define the matrix A
A = np.array([[4, 0, 1], [2, 3, 2], [64, 0, 4]])

# Find the eigenvalues of A
eigenvalues = np.linalg.eigvals(A)

# For each eigenvalue, compute λI - A and find its rank
for λ in eigenvalues:
    λI_minus_A = λ * np.eye(A.shape[0]) - A
    rank = np.linalg.matrix_rank(λI_minus_A)
    print(f"For eigenvalue λ = {λ}, the rank of λI - A is {rank}")
    
    # Find the eigenvalues of A
eigenvalues = np.linalg.eigvals(A)

# Assume A is diagonalizable until proven otherwise
is_diagonalizable = True

# For each eigenvalue, compute λI - A and find its rank
for λ in eigenvalues:
    λI_minus_A = λ * np.eye(A.shape[0]) - A
    rank = np.linalg.matrix_rank(λI_minus_A)
    if rank != A.shape[0] - 1:
        is_diagonalizable = False
        break

print("A is", "diagonalizable" if is_diagonalizable else "not diagonalizable")


# Find the eigenvalues of A
eigenvalues = np.linalg.eigvals(A)

# Sort the eigenvalues in ascending order
eigenvalues_sorted = np.sort(eigenvalues)

# Assume A is diagonalizable until proven otherwise
is_diagonalizable = True

# For each eigenvalue, compute λI - A and find its rank
for λ in eigenvalues_sorted:
    λI_minus_A = λ * np.eye(A.shape[0]) - A
    rank = np.linalg.matrix_rank(λI_minus_A)
    if rank != A.shape[0] - 1:
        is_diagonalizable = False
        break

print("A is", "diagonalizable" if is_diagonalizable else "not diagonalizable")