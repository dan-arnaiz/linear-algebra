import numpy as np

u = np.array([5, 6])
v = np.array([8, -6])

# Calculate the dot product of u and v
dot_product = np.dot(u, v)

# Calculate the magnitudes of u and v
magnitude_u = np.linalg.norm(u)
magnitude_v = np.linalg.norm(v)

# Calculate the cosine of the angle between u and v
cos_theta = dot_product / (magnitude_u * magnitude_v)

print("Cosine of the angle between u and v: ", cos_theta)