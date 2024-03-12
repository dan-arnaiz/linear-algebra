import numpy as np

u = np.array([3, -1, -6, 1, 0, 8, -5, 1])
v = np.array([-2, -1, 0, 6, 5, 3, -2, 1])

# Calculate the Euclidean distance between u and v
distance = np.linalg.norm(u - v)

print("d(u, v) = ", distance)

squared_distance = distance**2
print("d(u, v)^2 = ", squared_distance)