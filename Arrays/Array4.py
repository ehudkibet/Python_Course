#Slicing
#Slicing in python means taking elements from one given index to another given index.

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #Doesn't include end. Includes start

#Slice elements from index 4 to the end of the array

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

#Negative slicing
#Slice from the index 3 from the end to index 1 from the end
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

#Slicing 2-D Arrays
#From the second element, slice elements from index 1 to index 4 (not included)
arr1= np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr1[1, 1:4])

#From both elements, return index 2
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr1[0:2, 2])
