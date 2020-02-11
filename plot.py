import matplotlib.pyplot as plt
import numpy as np
import os

data=np.loadtxt("ASG_96_len112_known_last12_2.txt")

plt.plot(data[0],data[1])
plt.show()
print(data.shape)