#Python Program to input .txt data and generate a plot using it

#import modules
import numpy as np
import matplotlib.pyplot as plt

#Input the data
data=np.loadtxt('Scatter.txt')
x=data[:,0] #Position
x_err=0.3

y1=data[:,1]  #Position
y1_err=data[:,2] #Position

y2=data[:,3] #Position
y2_err=data[:,4] #Position

#plot figure
plt.figure()
plt.errorbar(x,y1,xerr=x_err,yerr=y1_err,color="blue",capsize=0,ls='none',elinewidth=0.6)
plt.errorbar(x,y2,xerr=x_err,yerr=y2_err, color="red",capsize=0, ls='none',elinewidth=0.6)

plt.plot(x,y1,color="blue",linestyle='None',marker='o',markersize=5,label='Male')
plt.plot(x,y2,color='red',linestyle='None',marker='*', markersize=6 , label='Female')

#Label the Figure

plt.title('Brain Analysis Test')
plt.xlabel('Age(Years)')
plt.ylabel('Average Points(Alien Score)')
plt.legend

#Show the plot on a screen
plt.show()