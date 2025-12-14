
"""
NumPy Data Explorer
Project 1 - Syntecxhub Internship

This script demonstrates:
- NumPy array creation
- Indexing & slicing
- Mathematical & statistical operations
- Reshaping & broadcasting
- Save & load NumPy arrays
- Performance comparison with Python lists
"""

import numpy as np
import time

# Array creation
arr = np.array([1, 2, 3, 4, 5])
matrix = np.arange(1, 10).reshape(3, 3)

print("Array:", arr)
print("Matrix:\n", matrix)

# Indexing & slicing
print("First element:", arr[0])
print("First row:", matrix[0])

# Mathematical operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))

# Axis-wise operation
print("Column-wise sum:", np.sum(matrix, axis=0))

# Reshaping & broadcasting
reshaped = arr.reshape(5, 1)
broadcasted = reshaped + 10
print("Broadcasted array:\n", broadcasted)

# Save & load
np.save("sample_array.npy", arr)
loaded = np.load("sample_array.npy")
print("Loaded array:", loaded)

# Performance comparison
python_list = list(range(1000000))
numpy_array = np.arange(1000000)

start = time.time()
[x * 2 for x in python_list]
print("Python list time:", time.time() - start)

start = time.time()
numpy_array * 2
print("NumPy array time:", time.time() - start)
