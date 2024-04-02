import numpy as np
from scipy.integrate import quad

# Define the polynomials p and q
p = lambda x: -2 + 2*x + x**2
q = lambda x: 4 + 4*x - 5*x**2

# Define the inner product function
inner_product = lambda x: p(x) * q(x)

# Calculate the inner product <p, q>
result, error = quad(inner_product, -1, 1)

print("The inner product <p, q> is:")
print(result)


# Find the standard inner product on P2 of the given polynomials.
# p = -2+2x+x^2, q = 4+4x-5x^2

# <p, q> = ______