import numpy as np

a = np.array(1)
print(a)
print(type(a))

# 1-D array
b = np.array([1,2,3,4,5,6,7,8,9])
print(b[1])
print(b[4])
print(b[1] + b[8])

# 2-D array
c = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(c)
print(type[c])
print(c[0,1])
print(c[1,4])
print(c[0,4])
print(c[1,3])

# 3-D array
d = np.array ([[["a","b","c","d","e"], ["g","h","i","j","k"], ["l","m","n","o","p"]]])
e = np.array ([[["a","b","c","d","e"], ["g","h","i","j","k"]], [["l","m","n","o","p"], ["g","h","i","j","k"]]])
print(d)
print(type(d))
print(d[0,1,4])
print(e[1,0,2])
print(e[1,1,4])
print(e[1,1, -1])
print(e[1,0, -3])