#Python program to plot a sine and cosines waves

#import modules
import numpy as np
import matplotlib.pyplot as plt

#Compute x and y values for plotting
x=np.arange(0,4*np.pi,0.1)
#or x=np.linspace(0,4*np.pi,200)
y1=np.sin(x)
y2=np.cos(x)

#plot the figure
plt.figure()
plt.plot(x,y1,color="red",linestyle="--",linewidth=3,label="sine")#generate sine
plt.plot(x,y2, color="blue",linestyle="-",linewidth=3,label="cosine")#generate cosine

#Label the figure
plt.title("Sine Wave form")
plt.xlabel("Wavelength")
plt.ylabel("Amplitude")
plt.legend()


#Manipulate the axis limit
plt.xlim(0,6*np.pi)
plt.ylim(-1.5,1.5)

#Change the x-axis tick labels(To show pi)- optional
#Uncomment to see
plt.xticks([0*np.pi,1*np.pi,2*np.pi,3*np.pi,4*np.pi,5*np.pi,6*np.pi],['0','$\mathregular{\pi}$',
'2$\mathregular{\pi}$','3$\mathregular{\pi}$','4$\mathregular{\pi}$','5$\mathregular{\pi}$','6$\mathregular{\pi}$'])

#Show the plot on the screen
plt.show()

#output the plot to a file
#plt.savefig("sine.png")


