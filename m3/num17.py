import numpy as np

# Define the sets of vectors
sets = [
    [np.array([0, 5]), np.array([7, 0])],
    [np.array([-1/np.sqrt(2), 1/np.sqrt(2)]), np.array([1/np.sqrt(2), 1/np.sqrt(2)])],
    [np.array([-1/np.sqrt(6), -1/np.sqrt(6)]), np.array([1/np.sqrt(6), 1/np.sqrt(6)])],
    [np.array([0, 0]), np.array([0, 5])]
]

# For each set of vectors, check if they are orthogonal and orthonormal
for i, vectors in enumerate(sets, start=1):
    u, v = vectors
    orthogonal = np.dot(u, v) == 0
    orthonormal = orthogonal and np.linalg.norm(u) == 1 and np.linalg.norm(v) == 1
    print(f"Set {i} is {'orthogonal' if orthogonal else 'not orthogonal'}, "
          f"and is {'orthonormal' if orthonormal else 'not orthonormal'}")


# In each part, determine whether the set of vectors is orthogonal and whether it is orthonormal with respect to the euclidean inner product on Rsquared.
# (a) (0, 5), (7, 0)
# (b) (-1/√ 2, 1/√ 2), (1/√ 2, 1/√ 2)
# (c) (-1/√ 6, -1/√ 6), (1/√ 6, 1/√ 6)
# (d) (0, 0), (0,5)