#Calculating area prompting the user to input radius.
'''import math
r=float(input("Enter the radius:"))
print("The radius entered is", r)
area=round(math.pi*r*r)
print("The area of the circle is",area,"sq.cm")'''
#End

#Calculating 2 numbers
'''a=float (input("Enter the first number:"))
b=float (input("Enter the second number:"))
c=a+b
print("The sum is",c) '''

#   Calculate area of triangle using Hero's formula
import math
a=float(input("Enter length a:"))
b=float(input("Enter length b:"))
c=float(input("Enter length c:"))
s=(a+b+c)/2
z=(s-a)*(s-b)*(s-c)
area=round(math.sqrt(s*z))
print("The area is",area,"sq.cm")

