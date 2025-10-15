import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
fx = np.array([0.41, 0.37, 0.16, 0.05, 0.01])
cdf = np.cumsum(fx)

plt.step(x, cdf, where='post')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('CDF of X')
plt.ylim(0, 1.05)
plt.grid(True)
plt.show()
