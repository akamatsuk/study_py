import numpy as np
import matplotlib.pyplot as plt

#make graph data
x = np.arange(0, 6, 0.1)  #0~6 0.1plot
y1 = np.sin(x)
y2 = np.cos(x)

# graph
plt.plot(x, y1, label="sin")
plt.plot(x, y2,linestyle = "dashdot", label="cos")  
# supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend() #凡例
plt.show()
