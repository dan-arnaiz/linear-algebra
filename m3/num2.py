import numpy as np



# Let u = (2, -1, 1), v = (2, 0, -1) and w = (-4, 10, 19). 
# Evaluate the expression.
# || 2u - 3v + w || = _______


# Define the vectors u, v, w
u = np.array([2, -1, 1])
v = np.array([2, 0, -1])
w = np.array([-4, 10, 19])

# Calculate the expression 2u - 3v + w
expression = 2*u - 3*v + w

# Calculate the norm of the expression
norm_expression = np.linalg.norm(expression)

print("|| 2u - 3v + w || =", norm_expression)