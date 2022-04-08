import math as m
import cmath
a=float(input('a:'))
b=float(input('b:'))
c=float(input('c:'))
d=(b**2-(4*a*c))

x1=(-b+cmath.sqrt(d))/(2*a)
x2=(-b-cmath.sqrt(d))/(2*a)
print(x1,x2)
'''
if d>=0:
        print('root 1',(-b+m.sqrt(d))/(2*a))
        print('root 2',(-b-m.sqrt(d))/(2*a))
else:
              print('real part:',(-b/(2*a)),'-'+'j',((m.sqrt(-d))/(2*a)))
              print('real part:',(-b/(2*a)),'+'+'j',((m.sqrt(-d))/(2*a)))
'''
