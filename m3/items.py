import numpy as np


class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return str(self.coordinates)

    def add(self, other):
        return Vector([x + y for x, y in zip(self.coordinates, other.coordinates)])

    def subtract(self, other):
        return Vector([x - y for x, y in zip(self.coordinates, other.coordinates)])

    def dot_product(self, other):
        return sum(x * y for x, y in zip(self.coordinates, other.coordinates))

    def scalar_multiply(self, scalar):
        return Vector([x * scalar for x in self.coordinates])


# Example usage:
v1 = Vector([1, 2, 3])  # 3-space vector
v2 = Vector([4, 5, 6])  # 3-space vector

# print("v1:", v1)
# print("v2:", v2)
# print("v1 + v2:", v1.add(v2))
# print("v1 - v2:", v1.subtract(v2))
# print("v1 . v2:", v1.dot_product(v2))
# print("2 * v1:", v1.scalar_multiply(2))


#num1

Find the norm of v, and a unit vector, u = (u1, u2, u3) that is oppositely directed to the vector v = (7, 6, -6). Use the fact that if v is any nonzero vector, then v / ||v|| is a unit vector.

||v|| = _____ u = (_____, _____, _____)


# Define the vector v
v = np.array([7, 6, -6])

# Calculate the norm of v
norm_v = np.linalg.norm(v)
print("||v|| =", norm_v)

# Calculate the unit vector u that is oppositely directed to v
u = -v / norm_v
print("u =", tuple(u))

11.0 





Let u = (2, -1, 1), v = (2, 0, -1) and w = (-4, 10, 19). 
Evaluate the expression.
|| 2u - 3v + w || = _______

