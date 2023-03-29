import numpy as np

# Define the square array
arr = np.array([[3, -2], [1, 0]])

# Compute eigenvalues and eigenvectors
eig_values, eig_vectors = np.linalg.eig(arr)

# Print the eigenvalues and eigenvectors
print("Eigenvalues: ", eig_values)
print("Eigenvectors: \n", eig_vectors)
