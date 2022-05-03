import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)


radius = [0.33, 0.66, 0.98, 1.31, 1.64, 1.97]

for i in range(len(radius)):
    plt.plot(radius[i]*np.cos(theta), radius[i]*np.sin(theta), label=str(i))


plt.xlim(-3, 3)
plt.ylim(-3, 3)

plt.grid(linestyle='--')

plt.title('How to plot a circle with matplotlib ?', fontsize=8)

plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')

plt.show()
