# 27] WAP to create a 3*3 numpy array with all the elements as per the user choice and print
# the sum of all elements of the array.
import numpy as np

# Function to create a 3x3 array with user input elements
def create_array():
    elements = []
    for _ in range(3):
        row = []
        for _ in range(3):
            element = float(input("Enter element for the array: "))
            row.append(element)
        elements.append(row)
    return np.array(elements)

# Create the array
array = create_array()

# Print the array
print("Array:")
print(array)

# Print the sum of all elements in the array
print("Sum of all elements:", np.sum(array))
