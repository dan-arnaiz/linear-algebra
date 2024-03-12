import numpy as np

u = np.array([1, -1, 2])
v = np.array([4, 1, 1])
w = np.array([10, -3, 6])

resultant_vector = 6*u - 2*v + w
norm = np.linalg.norm(resultant_vector)

print(norm)


u = np.array([0, 5, -6])
v = np.array([8, 0, 2])  # replace x with the appropriate value

dot_product = np.dot(u, v)
print(dot_product)

# Dot product of u and v
dot_product_uv = np.dot(u, v)
print("Dot product of u and v: ", dot_product_uv)

# Dot product of u and u
dot_product_uu = np.dot(u, u)
print("Dot product of u and u: ", dot_product_uu)

# Dot product of v and v
dot_product_vv = np.dot(v, v)
print("Dot product of v and v: ", dot_product_vv)

//

