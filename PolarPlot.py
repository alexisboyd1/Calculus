"""
Demo of a line plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt



theta = np.arange(0, 2*np.pi,.01)
r = 1 -np.cos(theta)
ax = plt.subplot(111, polar=True)
ax.plot(theta, r, color='r', linewidth=3)
ax.set_rmax(2.0)
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
