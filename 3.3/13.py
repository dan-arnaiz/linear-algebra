import numpy as np
from scipy.linalg import orth

# Define the vectors
v1 = np.array([1, 5, -4])
v2 = np.array([3, 14, 1])
v3 = np.array([1, 4, 9])

# Stack the vectors into a matrix
V = np.vstack((v1, v2, v3))

# Find an orthonormal basis for the column space of V
Q, R = np.linalg.qr(V)

# The last row of Q gives a basis for the orthogonal complement
w1 = Q[-1]

print("A basis for the orthogonal complement is w1 =", w1)

# The last row of Q gives a basis for the orthogonal complement
w1 = Q[-1]

# Normalize w1 by its last component
w1_normalized = w1 / w1[-1]

print("A basis for the row space is w1 =", w1_normalized)