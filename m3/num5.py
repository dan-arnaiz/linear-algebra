import numpy as np

# Define the vectors u and a
u = np.array([-6, -2])
a = np.array([3, -9])

# Calculate the vector component of u along a
u_along_a = (np.dot(u, a) / np.linalg.norm(a)**2) * a

# Calculate the vector component of u orthogonal to a
u_orthogonal_a = u - u_along_a

print("Vector component of u along a =", tuple(u_along_a))
print("Vector component of u orthogonal to a =", tuple(u_orthogonal_a))





# Let u = (-6, -2) and a = (3, -9). Find the vector component of u along a and the vector component of u orthogonal to a.

# Vector component of u along a = (_____, _____)

# Vector component of u orthogonal to a = (_____, _____)