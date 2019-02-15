import random
import math

class Boid:
    def __init__(self, lb, ub):
        self.position = [random.uniform(lb[i], ub[i]) for i in range(len(lb))]
        self.velocity = [0 for _ in range(len(lb))]

class BoidsAlgorithm:
    def __init__(self, size, lb, ub):
        self.dim = len(lb)        
        self.boids = [Boid(lb, ub) for _ in range(size)]
        self.__on_update = None

    def set_on_update(self, callback):
        self.__on_update = callback

    def __distance(self, b1, b2):
        dist = 0
        for dim in range(self.dim):
            dist += (b2.position[dim] - b1.position[dim])**2

        return math.sqrt(dist)

    def __cohesion(self, boid):
        coef = .1
        cohesion = [0 for _ in range(self.dim)]
        
        for b in self.boids:
            if b != boid:
                for dim in range(self.dim):
                    cohesion[dim] += b.position[dim]
        
        for dim in range(self.dim):
            cohesion[dim] /= (len(self.boids) - 1)
        
        result = [0 for _ in range(self.dim)]
        for dim in range(self.dim):
            result[dim] = (cohesion[dim] - boid.position[dim]) * coef

        return result

    def __separation(self, boid):
        min_distance = 10
        separation = [0 for _ in range(self.dim)]

        for b in self.boids:
            if b != boid and self.__distance(boid, b) < min_distance:
                for dim in range(self.dim):
                    separation[dim] -= (b.position[dim] - boid.position[dim])

        return separation


    def __alignment(self, boid):
        coef = .25
        alignment = [0 for _ in range(self.dim)]
        
        for b in self.boids:
            if b != boid:
                for dim in range(self.dim):
                    alignment[dim] += b.velocity[dim]
        
        for dim in range(self.dim):
            alignment[dim] /= (len(self.boids) - 1)
        
        result = [0 for _ in range(self.dim)]
        for dim in range(self.dim):
            result[dim] = (alignment[dim] - boid.velocity[dim]) * coef

        return result

    def update(self):
        for boid in self.boids:
            cohesion = self.__cohesion(boid)
            separation = self.__separation(boid)
            alignment = self.__alignment(boid)
            
            for dim in range(self.dim):
                boid.velocity[dim] += cohesion[dim] + separation[dim] + alignment[dim]
                boid.position[dim] += boid.velocity[dim]

            if callable(self.__on_update):
                self.__on_update(self.boids)

    def run(self, iters):
        for _ in range(iters):
            self.update()
    
if __name__ == '__main__':
    pass