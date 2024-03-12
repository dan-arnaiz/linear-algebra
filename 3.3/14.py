from sympy import symbols, Eq, solve

# Define the vectors
u = [2, 8, 2]
v = [8, 10]

# Define the symbol k
k = symbols('k')

# Set the dot product of u and v equal to zero and solve for k
equation = Eq(u[0]*v[0] + u[1]*v[1] + u[2]*k, 0)
solution = solve(equation, k)

print("The values of k that make u and v orthogonal are:", solution)