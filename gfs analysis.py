import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# 2D plot of gfs for different altitudes
plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)

y = 3*2**3/(x**2)
y = [3*2**3/(i**2) if i > 2 else 3*i for i in x]

# plot
fig, ax = plt.subplots()

# add data
ax.plot(x, y, linewidth=2.0)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

# add axis labels
ax.set_xlabel('r')
ax.set_ylabel('g')

plt.show()


# 3D plot of gfs for different earth radii and altitudes
plt.style.use('_mpl-gallery')

# Make data
# X = np.arange(0, 6378100, 10000) # 6378100m is the radius of earth
# Z = np.arange(0, 6378100, 10000)
X = np.arange(0, 300, 1)
Z = np.arange(0, 100, 1)
X, Z = np.meshgrid(X, Z)
Y = []

# Define the gravitational constant
G = 6.67408e-11
# Define the density of the earth
P = 5514

y=0
for x2,z2 in zip(X,Z):
    y2=[]
    for x,z in zip(x2,z2):
        if x>z:
            # y = (G * z**3 * P * 4/3*np.pi) / x**2
            y = (z**3) / x**2
        else:
            # y = G * x * 4/3*np.pi*P
            y = x
        y2.append(y)
    Y.append(y2)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(Z, Y, X, cmap=cm.Blues)
# ax.plot_surface(Z, Y, X, cmap=cm.Blues)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
       
ax.set_xlabel('planet radius')
ax.set_ylabel('g')
ax.set_zlabel('r')

ax.view_init(elev=-163, azim=-27, roll=100)

plt.show()