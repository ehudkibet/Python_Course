import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel(‘radiation1.xls’)
theta=data.theta
power=data.power_norm_dB
theta = np.deg2rad(theta)
ax = plt.subplot(111, projection=‘polar’)
ax.plot(theta, power,color=‘red’)
ax.set_rmax(0)
ax.set_rticks([-18,-15, -12,-9,-6,-3,0])
ax.set_rlabel_position(-22.5)
ax.grid(True)
plt.show()