import numpy as np

# Define the coefficients of the line equation and the point
a, b, d = 5, 8, 0  # replace 0 with the actual value of d if known
x0, y0 = -8, 3

# Calculate the distance from the point to the line
D = abs(a*x0 + b*y0 + d) / np.sqrt(a**2 + b**2)

print("D = ", D)