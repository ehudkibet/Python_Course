#Reshaping
#Reshaping means changing the shape of an array. The shape of an array is the number of elements in each dimension.

#Example: Convert the following 1-D array with 12 elements into a 2-D array.
#The outermost dimension will have 4 arrays, each with 3 elements.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(4, 3)
print(new_arr)
arr2=arr.reshape(2,6)
print(arr2)

# Convert the following 1-D array with 12 elements into a 3-D array.
#The outermost dimension will have 2 arrays that contains 3 arrays,each with 2 elements

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr1 = arr.reshape(2, 3, 2)
print(new_arr1)
