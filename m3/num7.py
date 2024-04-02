import numpy as np

# Define the vectors u, v, w
u = np.array([1, 1, -4])
v = np.array([0, 3, -5])
w = np.array([1, 7, 4])

# (a) u x v
cross_uv = np.cross(u, v)
print("(a) u x v =", tuple(cross_uv))

# (b) -u x v
cross_neg_u_v = np.cross(-u, v)
print("(b) -u x v =", tuple(cross_neg_u_v))

# (c) u x (v + w)
cross_u_v_w = np.cross(u, v + w)
print("(c) u x (v + w) =", tuple(cross_u_v_w))

# (d) w . (w x v)
dot_w_cross_w_v = np.dot(w, np.cross(w, v))
print("(d) w . (w x v) =", dot_w_cross_w_v)

# (e) w x w
cross_ww = np.cross(w, w)
print("(e) w x w =", tuple(cross_ww))

# (f) (5v - 2u) x (5v - 2u)
cross_5v_2u = np.cross(5*v - 2*u, 5*v - 2*u)
print("(f) (5v - 2u) x (5v - 2u) =", tuple(cross_5v_2u))





# Let u = (1, 1, -4), v = (0, 3, -5), and w = (1, 7, 4).
# Compute the indicated vectors.

# (a) u x v = (__ , __ , __)
# (b) -u x v = (__ , __ , __)
# (c) u x (v + w) = (__ , __ , __)
# (d) w . (w x v) = (__ , __ , __)
# (e) w x w  = (__ , __ , __)
# (f) (5v - 2u) x (5v - 2u)  = (__ , __ , __)