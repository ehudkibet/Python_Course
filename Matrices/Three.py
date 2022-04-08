#Solving quadratic equation
"""
Write a python code to solve the quadratic equation ax**2 + bx + c = 0;
(i) coefficients provided in the script and
(ii) user prompted to enter the coefficients a, b and c

"""

import numpy as np

# import complex math module
import cmath

 #a)PART ONE
a=1
b=5
c=6

 #Calculate discriminant
d=(b**2)-(4*a*c)

 #Find two solutions
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print("The solution are".format(sol1,sol2))

#PART B
A=float(input("Enter A:"))
B=float(input("Enter B:"))
C=float(input("Enter C:"))

#Calculate discriminant
D=(B**2)-(4*A*C)
soln1=(-B+cmath.sqrt(D))/(2*A)
soln2=(-B-cmath.sqrt(D))/(2*A)

print(soln1)
print(soln2)

'''
#Convert list to array
list=[1,2,3,4]
arr=np.array([list],int)
print(arr)

'''
