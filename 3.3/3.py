import numpy as np

u = np.array([-2, 1, 3])
v = np.array([6, 1, -6])
w = np.array([-6, 2, 5])

# Compute the cross product of v and w
cross_product = np.cross(v, w)

# Compute the dot product of u and the cross product
scalar_triple_product = np.dot(u, cross_product)

print("u . (v x w) = ", scalar_triple_product)