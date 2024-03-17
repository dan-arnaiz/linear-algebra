import numpy as np

# Define the matrix A
A = np.array([[-6j, 4], [3-1j, 1+4j]])

# Find the conjugate of A
A_conj = np.conj(A)

# Find the real part of A
A_real = np.real(A)

# Find the imaginary part of A
A_imag = np.imag(A)

# Find the determinant of A
A_det = np.linalg.det(A)

# Find the trace of A
A_trace = np.trace(A)

print("The conjugate of A is:")
print(A_conj)

print("The real part of A is:")
print(A_real)

print("The imaginary part of A is:")
print(A_imag)

print("The determinant of A is:")
print(A_det)

print("The trace of A is:")
print(A_trace)


# Let A = [[-6i, 4, [3-i, 1+4i]]
# Find Ā, Re(A), Im(A), det(A), and tr(A).A

