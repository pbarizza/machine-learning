import numpy as np
from matplotlib import pyplot as plt

A = np.array([[0.5, 0.5, 0.25], [0.25, 0, 0.25], [0.25, 0.5, 0.5]])

xtoday = [1, 0, 0]

# Matrix-vector multiplication
A @ xtoday

the_weather = np.zeros((50, 3))
the_weather[0, :] = xtoday
for i in range(50):
    xtomorrow = A @ xtoday  # xtomorrow is linear combination of xtoday
    xtoday = xtomorrow
    the_weather[i, :] = xtomorrow

plt.plot(the_weather)
plt.grid(True)
