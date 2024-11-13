import numpy as np 

a = np.array([[1,2,3],[4,5,6]])
print("Before swapp matrix")
print(a)
a[[0,1]] = a[[1,0]]
print("\n After waping matrix")
print(a)