from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

# define 2d function
def f(x, y):
   return x*y

# set area
xmin, xmax = -1, 1
ymin, ymax = -1, 1

# set resolution for wireframe (intervals to devide (xmin, xmax), (ymin, ymax) into)
xresw, yresw = 30, 60

# set resolution for heatmap (intervals to devide (xmin, xmax), (ymin, ymax) into)
xresh, yresh = 50, 100


xh = np.linspace(xmin, xmax, xresh)
yh = np.linspace(ymin, ymax, yresh)

xw = np.linspace(xmin, xmax, xresw)
yw = np.linspace(ymin, ymax, yresw)

Xw, Yw = np.meshgrid(xw, yw)
Zw = f(Xw, Yw)

Xh, Yh = np.meshgrid(xh, yh)
Zh = f(Xh, Yh)

fig, axs = plt.subplots(1, 2, subplot_kw={"projection": "3d"})

axs[0].plot_wireframe(Xw, Yw, Zw)
axs[0].set_title('Wireframe')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_zlabel('f(x)')

surf = axs[1].plot_surface(Xh, Yh, Zh, cmap=cm.coolwarm, linewidth=0, antialiased=False)
axs[1].zaxis.set_major_locator(LinearLocator(10))
fig.colorbar(surf, shrink=0.4, aspect=50)
axs[1].set_title('Heatmap')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].set_zlabel('f(x)')

plt.show()
