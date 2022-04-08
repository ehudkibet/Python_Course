import numpy as np
#Creating an array
arr=np.array([1,2,3,4,5,6])
print(arr)
print(type(arr)) #Type is numpy.ndarray

myarray=np.array([1,'Yes','False',30])
print(myarray)

#Convert list and tuple to array
arr1=np.array((1,2,3,4,5))
print(arr1)
print(type(arr1))

#we use arrays in stead of lists because mathematical operations can be carried out on arrays without iterating
#It also stores data in a compact form

list=[1,2,3,4,5,6]
#list2=list/3 - will give error

my_Array=np.array([1,2,3,4,5,6])
arrDiv=my_Array/3
print(arrDiv)