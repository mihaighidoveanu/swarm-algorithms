import numpy as np
import matplotlib.pyplot as plt
import Boids

size = 5
lb = [0,0]
ub = [1000,1000]
iters = 1000

def update(boids):
    plt.axis([lb[0], ub[0], lb[1], ub[1]])    
    
    for boid in boids:
        for dim in range(len(boid.position)):
            if boid.position[dim] > ub[dim]:
                boid.position[dim] -= ub[dim]
            if boid.position[dim] < lb[dim]:
                boid.position[dim] += ub[dim]

        plt.plot(boid.position[0], boid.position[1], 'g^')
    
    plt.pause(.04)
    plt.clf()

plt.ion()        

boidsAlgorithm = Boids.BoidsAlgorithm(size, lb, ub)
boidsAlgorithm.set_on_update(update)

boidsAlgorithm.run(iters)
plt.show()
plt.ioff()
