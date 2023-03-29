import numpy as np

# Define the original array
arr = np.array([[1, 2], [3, 4], [5, 6]])

# Reshape the array to 2x3
arr_2x3 = arr.reshape(2, 3)

# Reshape the array back to 3x2
arr_3x2 = arr_2x3.reshape(3, 2)

# Print the original array and the two reshaped arrays
print("Original array:\n", arr)
print("Reshaped to 2x3:\n", arr_2x3)
print("Reshaped back to 3x2:\n", arr_3x2)
