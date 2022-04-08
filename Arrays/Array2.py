#Dimensions in Arrays
#A dimension in an array is a level of array depth

import numpy as np

''''#a) 0-D arrays or Scalars
myArray=np.array(45)
#print(type(myArray))
print(myArray.ndim) #To know dimension. It will be dimension 0 since it is not borrowed from a list. Were it a list ,
# it would be dimension 1 as seen bellow

#b)1-D array or unidimensional
myArray1=np.array([1])
print(myArray1.ndim) #Check dimension

myArray2=np.array([1,2,3,4,5])
#print(myArray2)
print(myArray2.ndim) #One dimension still

#c) 2-D array
myArray3=np.array([[1,2,3],[2,3,4]])
print(myArray3) #No commas and only square brackets
print(myArray3.ndim)  # 2 Dimensional
print(myArray3.shape) #shape is (2,3)

#d) 3-D array
myArray4=np.array([[[1,2,3],[2,3,4],[3,4,7]]]) #3D has 2 square brackets before the brackets that encompass each list.
print(myArray4)
print(myArray4.ndim)
print(myArray4.shape) # shape is (1,3,3)'''

#e) Higher dimensional arrays
#An array can have any number of dimensions. You can define the dimensions by using the ndmin argument
#We'll create a 5D array below
myArray5=np.array([1,2,3,4],ndmin=5)
print(myArray5)
print(myArray5.ndim)