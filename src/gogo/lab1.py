# Sisteme Swarm & MultiAgent Lab.1
# Particle Swarm Optimization

from benchmark import Rosenbrock, Rastrigin, Griewank
import PSO 

pso = PSO.PSO()
    
print('Rosenbrock: {0}'.format(pso.run(100, Rosenbrock, (-3,-3), (3,3))))
print('Rastrigin: {0}'.format(pso.run(100, Rastrigin, (-5.12,-5.12), (5.12,5.12))))
print('Griewank: {0}'.format(pso.run(100, Griewank, (-600,-600), (600,600))))