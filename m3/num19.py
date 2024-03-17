import numpy as np

# Define the vectors u, v, and w
u = np.array([7, -1, 0, 3, -3])
v = np.array([1, 1, 9, -4, 0])
w = np.array([-8, 2, -4, -6, 3])

# Calculate -2(3w+v)+(2u+w)
result = -2*(3*w + v) + (2*u + w)

print("The result is:")
print(result)


# Let u = (7, -1, 0, 3, -3), v = (1, 1, 9, -4, 0), and w = (-8, 2, -4, -6, 3). Find -2(3w+v)+(2u+w)