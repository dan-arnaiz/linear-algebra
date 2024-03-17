import numpy as np


# Find the Euclidean inner product u.v, u.u, and v.v

# u = (0, 8, 0) and v = (1, -5, 7)

# u.v = _____ u.u = _____ v.v = _____

# Define the vectors u and v
u = np.array([0, 8, 0])
v = np.array([1, -5, 7])

# Calculate the inner products
uv = np.dot(u, v)
uu = np.dot(u, u)
vv = np.dot(v, v)

print("u.v =", uv)
print("u.u =", uu)
print("v.v =", vv)