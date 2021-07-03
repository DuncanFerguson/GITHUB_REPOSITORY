import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0, 10, 101)
sin = np.sin(x_values)
cos = np.cos(x_values)
fig = plt.figure()
dist = np.random.normal(size=101)

ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(323)
ax3 = fig.add_subplot(325)
ax4 = fig.add_subplot(222)
ax5 = fig.add_subplot(224)

ax1.plot(x_values, sin)
ax2.plot(x_values, cos)
ax3.plot(x_values, x_values + 5)
ax4.hist(dist)
ax5.scatter(x_values, dist)

plt.show()

