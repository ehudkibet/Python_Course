import math

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,4*np.pi,0.1)
y1=np.sinc(x)
y2=np.cos(x)

plt.figure()
plt.plot(x,y1,color="red",linestyle="--",linewidth=3,label="sine")
plt.plot(x,y2, color="blue",linestyle="-",linewidth=3,label="cosine")

plt.title("Sine Wave form")
plt.xlabel("Wavelength")
plt.ylabel("Amplitude")
plt.legend()

plt.xticks([-2*np.pi,-1*np.pi,0*np.pi,1*np.pi,2*np.pi],['-2$\mathregular{\pi}$','-1$\mathregular{\pi}$','0','1$\mathregular{\pi}$','2$\mathregular{\pi}$',])
plt.show()

plt.savefig('cos.png')
