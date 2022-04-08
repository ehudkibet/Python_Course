import numpy as np

#input two matrices
#3 by 3 matrix
a=np.array([[3,3,5],[1,2,3],[1,1,1]],int)
b=np.array([[1,2,3],[3,4,5],[1,2,3]],int)

res_dot=np.dot(a,b) #Dot multiplication
print(res_dot)

res_mult=np.mat(a)*np.mat(b) #Method 2 of multiplication
print(res_mult)

res_add=np.mat(a)+np.mat(b)  #Addition
print(res_add)

res_cross=np.cross(a,b) #Cross multiplication
print(res_cross)

#python code to solve 2 by 2 matrix given in the module
A=np.array([[1,3],[2,4]],int)
B=np.array([[4,-2],[-3,1]],int)
C=np.array([[1,2],[2,1]],int)

res=np.dot(A,B)+2*C
print(res)
print(res.shape)
print(res.size)

