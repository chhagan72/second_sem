# 29] WAP to perform basic arithmetic operations on 1D and 2D array .
import numpy as np

# Create 1D array
array1d = np.array([1, 2, 3, 4, 5])

# Create 2D array
array2d = np.array([[1, 2, 3], [4, 5, 6]])

# Addition
print("Addition:")
print("1D array + 5:", array1d + 5)
print("2D array + 2:")
print(array2d + 2)

# Subtraction
print("\nSubtraction:")
print("1D array - 2:", array1d - 2)
print("2D array - 1:")
print(array2d - 1)

# Multiplication
print("\nMultiplication:")
print("1D array * 3:", array1d * 3)
print("2D array * 2:")
print(array2d * 2)

# Division
print("\nDivision:")
print("1D array / 2:", array1d / 2)
print("2D array / 3:")
print(array2d / 3)

# Element-wise square root
print("\nSquare Root:")
print("Square root of 1D array:", np.sqrt(array1d))
print("Square root of 2D array:")
print(np.sqrt(array2d))

# Element-wise exponential
print("\nExponential:")
print("Exponential of 1D array:", np.exp(array1d))
print("Exponential of 2D array:")
print(np.exp(array2d))
