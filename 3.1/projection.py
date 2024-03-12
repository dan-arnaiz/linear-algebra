import numpy as np

u = np.array([1, -3])
a = np.array([4, -3])

# Calculate the dot product of u and a
dot_product = np.dot(u, a)

# Calculate the norm of a
norm_a = np.linalg.norm(a)

# Calculate the norm of the projection of u onto a
norm_proj_u_a = abs(dot_product / norm_a) * norm_a

print("||proj_u a|| = ", norm_proj_u_a)