# Numpy Create array
import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))


arr2 = np.array((1,2,3,4,5))
print(arr2)

# 1-D array

arr3 = np.array([1,2,3,4,5,6,7])
print(arr3)

# 2 - D array

arr4 = np.array([[1,2,3,4,5,6,7,8]])
print(arr4)

# 3 - D array
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr5)

#Check Number of Dimensions
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

a = np.array([1,2,3,4])
b = np.array([[1,2,3,4,5]])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a)
print(a.ndim)
print(b)
print(b.ndim)
print(b)
print(c.ndim)

arr6 = np.array([[1,2,3,4], [6,7,8,9]])
print(arr6)


arr7 = np.array(["chhagan","vaibhav","balaji"])
print(arr7)