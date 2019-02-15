import random


class Particle:
    def __init__(self, lb, ub):
        self.position = [random.uniform(lb[i], ub[i]) for i in range(len(lb))]
        self.best = list(self.position)
        self.velocity = [random.uniform(-1, 1) for _ in range(len(lb))]


class PSO:
    def __init__(self, SIZE=1000, OMEGA=.5, PHI_P=.5, PHI_G=.5):
        self.SIZE = SIZE
        self.OMEGA = OMEGA
        self.PHI_P = PHI_P
        self.PHI_G = PHI_G
        self.__on_iter_handler = None
        
    def set_iter_handler(self, callback):
        self.__on_iter_handler = callback

    def run(self, iters, fitness, lb, ub):
        '''
            fitness function
            lb lower bound is tuple of 2
            ub upper bound is tuple of 2
            iters number of iterations
        '''

        particles = [Particle(lb, ub) for _ in range(self.SIZE)]

        global_best = list(particles[0].best)

        for particle in particles:
            if fitness(particle.best) < fitness(global_best):
                global_best = list(particle.best)

        for iter in range(iters):            
            for particle in particles:
                for dim in range(len(lb)):
                    rp = random.uniform(0, 1)
                    rg = random.uniform(0, 1)

                    particle.velocity[dim] = self.OMEGA * particle.velocity[dim] + \
                                             self.PHI_P * rp * (particle.best[dim] - particle.position[dim]) + \
                                             self.PHI_G * rg * (global_best[dim] - particle.position[dim])

                    particle.position[dim] += particle.velocity[dim]

                if fitness(particle.position) < fitness(particle.best):
                    particle.best = list(particle.position)
                    if fitness(particle.best) < fitness(global_best):
                        global_best = list(particle.best)
            
            if callable(self.__on_iter_handler):
                self.__on_iter_handler(particles, iter)

        return global_best
