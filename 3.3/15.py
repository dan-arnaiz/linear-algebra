from sympy import symbols, Eq, solve

# Define the point P and the normal n
P = [-1, 3, -2]
n = [-3, 1, -1]

# Define the symbols x, y, z
x, y, z = symbols('x y z')

# Define the position vector r
r = [x, y, z]

# Compute the dot product of n and (r - P)
dot_product = sum(n[i]*(r[i] - P[i]) for i in range(3))

# Set the dot product equal to zero to find the equation of the plane
equation = Eq(dot_product, 0)

print("The point-normal form of the equation of the plane is:", equation)