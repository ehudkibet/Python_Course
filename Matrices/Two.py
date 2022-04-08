#Solving linear equation
"""
2a+b+c=4
a+3b+2c=5
a=6
"""
import numpy as np
a=np.array([[2,1,1],[1,3,2],[1,0,0]],int)
b=np.array([4,5,6],int)
# linalg.solve is the function of NumPy to solve a system of linear scalar equations
res=np.linalg.solve(a,b)
print(res)