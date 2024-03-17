import numpy as np

# 6.1 Inner Products
# Define two vectors
v = np.array([1, 2, 3])
w = np.array([4, 5, 6])

# Calculate inner product
inner_product = np.dot(v, w)
print("Inner product of v and w:", inner_product)

# 6.3 Gram-Schmidt Process; QR-Decomposition
# Define a matrix
A = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])

# Perform QR decomposition
Q, R = np.linalg.qr(A)

print("Q (orthonormal basis):", Q)
print("R (upper triangular matrix):", R)


Find the norm of v, and a unit vector, u = (u1, u2, u3) that is oppositely directed to the vector v = (7, 6, -6). Use the fact that if v is any nonzero vector, then v / ||v|| is a unit vector.

||v|| = _____
u = (_____, _____, _____)
