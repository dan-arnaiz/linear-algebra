import math

# Define the point and the coefficients of the line
x0, y0 = -2, 7
a, b, c = 4, 5, 1

# Compute the distance from the point to the line
d = abs(a*x0 + b*y0 + c) / math.sqrt(a**2 + b**2)

# Print the distance rounded to one decimal place
print("The distance between the point and the line is:", round(d, 1))