import numpy as np

# Define the normal vector and the point
n = np.array([-4, 1, -1])
p = np.array([-1, 3, -4])

# Define a general point on the plane
r = np.array(['x', 'y', 'z'])

# Calculate the dot product of the normal vector and the difference between the general point and the specific point
dot_product = np.dot(n, (r - p))

# Print the equation of the plane
print(f"{dot_product} = 0")