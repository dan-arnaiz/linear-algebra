import numpy as np

u = np.array([7, 4, -1])
v = np.array([0, 5, -4])
w = np.array([4, 7, 5])

# Compute the cross product of v and w
cross_product_v_w = np.cross(v, w)

# Compute the cross product of u and (v x w)
result = np.cross(u, cross_product_v_w)

print("u x (v x w) = ", result)