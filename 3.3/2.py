import numpy as np

u = np.array([4, -6, 3])
v = np.array([0, 4, -6])
w = np.array([4, 9, -1])

# Compute the cross product of v and w
cross_product = np.cross(v, w)

# Compute the dot product of u and the cross product
scalar_triple_product = np.dot(u, cross_product)

# The volume of the parallelepiped is the absolute value of the scalar triple product
volume = abs(scalar_triple_product)

print("Volume = ", volume)