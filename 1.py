import numpy as np

# create random vector of size 15 having only integers in the range 1-20
vector = np.random.randint(low=1, high=21, size=15)

# reshape the array to 3 by 5
reshaped_array = np.reshape(vector, (3, 5))

# print array shape
print("Array shape:", reshaped_array.shape)
print(reshaped_array)
# Replace the max in each row by 0
reshaped_array[np.arange(len(reshaped_array)), np.argmax(reshaped_array, axis=1)] = 0

# print the modified array
print("Replaced the max in each row by 0", reshaped_array)

# Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements)
two_dim_array = np.zeros((4, 3), dtype=np.int32)

# Print array shape, type and data type
print("Array shape:", two_dim_array.shape)
print("Array type:", type(two_dim_array))
print("Array data type:", two_dim_array.dtype)
