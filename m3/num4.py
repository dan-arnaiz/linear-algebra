import numpy as np



# Find the cosine of the angle theta between u and v.

# u = (5, 2) and v = (6, -2)

# Round the final answer to the four decimal places.

# cos theta = ______


# Define the vectors u and v
u = np.array([5, 2])
v = np.array([6, -2])

# Calculate the dot product of u and v
dot_product = np.dot(u, v)

# Calculate the norms of u and v
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

# Calculate the cosine of the angle between u and v
cos_theta = dot_product / (norm_u * norm_v)

# Round the result to four decimal places
cos_theta = round(cos_theta, 4)

print("cos theta =", cos_theta)