import numpy as np

u = np.array([-3, 1, 3])
v = np.array([2, 0, -6])

# Compute the cross product of u and v
cross_product = np.cross(u, v)

print("The vector orthogonal to u and v is: ", cross_product)