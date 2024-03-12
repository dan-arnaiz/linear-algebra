import numpy as np

u = np.array([5, -1, 6])
v = np.array([0, 5, 4])

# Compute the cross product of u and v
cross_product = np.cross(u, v)

# The area of the parallelogram is the magnitude of the cross product
area = np.linalg.norm(cross_product)

print("Area = ", area)

# Original number
num = 46.70117771534247

# Round to 2 decimal places
rounded_num = round(num, 2)

print("Rounded number = ", rounded_num)