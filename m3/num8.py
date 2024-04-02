import numpy as np
import fractions

# Define the vectors u and v
u = np.array([8, 7, -6])
v = np.array([8, 7, 6])

# Calculate the cross product of u and v
cross_uv = np.cross(u, v)

# Calculate the norms of u, v and cross_uv
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
norm_cross_uv = np.linalg.norm(cross_uv)

# Calculate the sine of the angle between u and v
sin_theta = norm_cross_uv / (norm_u * norm_v)

print("sin theta =", sin_theta)


# Your decimal number
decimal_number = 0.8561191258578243

# Convert to a fraction
fraction = fractions.Fraction(decimal_number).limit_denominator()

print(f"The fraction representation of {decimal_number} is approximately {fraction}")


# Use the cross product to find the sine of the angle between the vectors u = (8, 7, -6) and v = (8, 7, 6).

# Note: Write the answer in exact form.


# sin theta = ____