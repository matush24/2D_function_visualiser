from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

# define 2d function
def f(tau, T):
   # tau = 0.5
   t0 = 1
   x=(2*t0-T)/tau
   x1=(t0-T)/tau
   x2=(-T)/tau
   xi = (np.arctan(x) + np.arctan(-x2))**-1
   return xi*((2*t0-T)*(np.arctan(x)-np.arctan(x1))-\
   (tau/2)*(np.log(1+x**2)-np.log(1+x1**2))+\
   (t0-T)*(np.arctan(x1)-np.arctan(x2))-\
   (tau/2)*(np.log(1+x1**2)-np.log(1+x2**2)))

   # return tau**-1 * xi * (1/(1 + ((t-T)/tau)**2)) 

print(f(0.4, 1))

# set area
xmin, xmax = 0, 2
ymin, ymax = 0, 2

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
axs[0].set_xlabel('tau')
axs[0].set_ylabel('T')
axs[0].set_zlabel('f(x)')

surf = axs[1].plot_surface(Xh, Yh, Zh, cmap=cm.coolwarm, linewidth=0, antialiased=False)
axs[1].zaxis.set_major_locator(LinearLocator(10))
fig.colorbar(surf, shrink=0.4, aspect=50)
axs[1].set_title('Heatmap')
axs[1].set_xlabel('tau')
axs[1].set_ylabel('T')
axs[1].set_zlabel('f(x)')

plt.show()