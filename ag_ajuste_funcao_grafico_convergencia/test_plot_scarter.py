import numpy as np
import matplotlib.pyplot as plt

def potential(A, B, C, x):
    result = A + (1/(B*np.sqrt(2*np.pi)))*np.exp(-((x-C)**2)/(2*(B**2)))
    return result

points = []
init = 1
for i in range(15):
    points.append([init,potential(45, 0.5, 3, init)])
    init += 0.2

x = [p[0] for p in points]
y = [p[1] for p in points]
# scarter black, with scatter points
plt.plot(x, y, 'o', label='scatter', markersize=3)
# add label
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
