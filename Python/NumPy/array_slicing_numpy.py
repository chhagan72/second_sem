""" 
Slicing arrays
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1
 """

import numpy as np 

d = np.array ([[["a","b","c","d","e"], ["g","h","i","j","k"], ["l","m","n","o","p"]]])
e = np.array ([[["a","b","c","d","e"], ["g","h","i","j","k"]], [["l","m","n","o","p"], ["g","h","i","j","k"]]])

print(d)
print(e)

print(d[0,1, :1])
print(e[0,0,1:5])
print(d[0, 1, -3:-1])
print(e[0,1, 1:4:2])
print(e[0,1, 1:2:3])
print(d[0,0, ::2])
print(d[0:2, 2])
print(d[0:1,0:2])
print(d[0:1,0:2,0:2])

arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[1:4])