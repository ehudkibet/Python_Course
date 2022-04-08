import numpy as np
#Array indexing -Accessing Array elements
#Starts with index 0
arr=np.array([1,2,3])
print(arr)
print(arr[2])

#Accessing arrays in a 2D array
arr1=np.array([[1,2],[2,3]])
#print(arr1.ndim)
print(arr1[0,0])
print(arr1[0,1])
print(arr1[1,0])
print(arr1[1,1])

#Accessing arrays in a 3D array
myArray3=np.array([[[1,2,3],[2,3,4],[3,4,7]]])
print(myArray3[0,0,2])
print(myArray3[0,2,2])

