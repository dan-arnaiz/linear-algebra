import numpy as np

# Define the vectors u and a
u = np.array([2, 1, 1, 2])
a = np.array([4, -4, 2, -2])

# Calculate the vector component of u along a
u_along_a = (np.dot(u, a) / np.linalg.norm(a)**2) * a

# Calculate the vector component of u orthogonal to a
u_orthogonal_a = u - u_along_a

print("Vector component of u along a =", tuple(u_along_a))
print("Vector component of u orthogonal to a =", tuple(u_orthogonal_a))

(0.2, -0.2, 0.1, -0.1)
(1.8, 1.2, 0.9, 2.1

# Let u = (2, 1, 1, 2) and a = (4, -4, 2, -2). Find the vector component of u along a and the vector component of u orthogonal to a.

# vector component of u along a = (_____, _____, _____, _____)

# vector component of u orthogonal to a = (_____, _____, _____, _____)