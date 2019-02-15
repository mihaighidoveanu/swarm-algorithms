from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

from benchmark import Rosenbrock, Rastrigin, Griewank
import PSO


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_zlim(-100, 100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

X = np.arange(-10, 10, .1)
Y = np.arange(-10, 10, .1)
X, Y = np.meshgrid(X, Y)
Z = np.zeros(X.shape)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i,j] = Rastrigin([X[i,j], Y[i,j]])

ax.plot_surface(X, Y, Z, cmap=cm.hot, linewidth=0, antialiased=False)

def plot_particles(particles, iter):
    if iter % 100 == 0:
        x = [particle.position[0] for particle in particles]
        y = [particle.position[1] for particle in particles]
        z = [Rosenbrock(particle.position) for particle in particles]
        ax.scatter(x, y, z, c='blue', linewidth=0, antialiased=False)

pso = PSO.PSO()
pso.set_iter_handler(plot_particles)
print(pso.run(100, Rosenbrock, (-3,-3), (3,3)))

plt.show()