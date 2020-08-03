import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()
#fig = plt.figure()
#fig.savefig("sin.pdf")   保存できない