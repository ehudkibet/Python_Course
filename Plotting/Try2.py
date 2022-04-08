#Joe Code
#import modules
import numpy as np
import matplotlib.pyplot as plt

#compute the x and y values for plotting points
x=np.arange(0,9*np.pi,0.2)
y=((np.sin(x))/(x))
g=[0, 5, 10, 15, 20, 25]
p=['zero', 'five', 'ten', 'fifteen', 'twenty', 'twenty five']

#plot figure
plt.figure
#plot using a line
#plt.plot(x,y,color='blue', linestyle='-',linewidth=2,label='Sine')

#plot using points ....uncoment to plot
plt.plot(x,y,color='blue',linestyle='None', marker='*',markersize=2,
label='Sine')
#labe the figure
plt.title('Sine Waveform')
plt.xlabel('Wavelength')
plt.ylabel('Amplitude')
plt.legend()
#grid
plt.grid(True)
#fit to screen
plt.tight_layout()
# you can display totally different values for x
plt.xticks(ticks=g, labels=p)
#Show the plot on the screen
plt.show()
#Output the plot to a file
#plt.savefig(‘Sine.png’)