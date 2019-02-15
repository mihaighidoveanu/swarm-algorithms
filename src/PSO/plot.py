# Reprezentarea grafica a suprafetei asociate functiei Rosenbrock

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import time

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-1.5, 2.1, 0.1)
Y = np.arange(-1.5, 2.1, 0.1)
X, Y = np.meshgrid(X, Y)
Z = np.zeros(X.shape)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i,j] = 100 * (Y[i,j] - X[i,j]**2) ** 2 + (1 - X[i,j]) ** 2

print(Z)

plt.ion() # activeaza modul de lucru interactiv;
          # se poate actualiza informatia dintr-o figura dupa
          # aparitia primei ferestre, fara a fi necesara inchiderea
          # ferestrei

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.scatter(1,2,100,c = 'r', marker = '+')

plt.show()

plt.pause(1)
# time.sleep(1)
# plt.clf() # sterge informatia reprezentata in grafic
plt.close()

fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.scatter(5,10,500,c = 'r', marker = '+')

plt.show()

plt.pause(100)


# plt.ioff() # dezactiveaza modul de lucru interactiv