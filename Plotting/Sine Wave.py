#Python program to plot a sine wave

#import modules
import numpy as np
import matplotlib.pyplot as plt

#Compute x and y values for plotting
x=np.arange(0,4*np.pi,0.1)
#or x=np.linspace(0,4*np.pi,200)
y=np.sin(x)

#plot the figure
plt.figure()
plt.plot(x,y,color="red",linestyle="--",linewidth=3,label="sine")

#Label the figure
plt.title("Sine Wave form")
plt.xlabel("Wavelength")
plt.ylabel("Amplitude")
plt.legend()

#Show the plot on the screen
plt.show()

#output the plot to a file
#plt.savefig("sine.png")


