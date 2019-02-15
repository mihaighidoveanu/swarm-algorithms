import random
import math

class Boid:
    def __init__(self, lb, ub):
        self.position = [random.uniform(lb[i], ub[i]) for i in range(len(lb))]
        self.velocity = [0 for _ in range(len(lb))]

class BoidsAlgorithm:
    def __init__(self, size, lb, ub):
        self.dim = len(lb)        
        self.lb = lb
        self.ub = ub
        self.boids = [Boid(lb, ub) for _ in range(size)]
        self.obstacles = []
        self.__on_update = None
        self.cohesion = True
        self.separation = True
        self.alignment = True
        self.dodge = True
        self.goal = False
        self.goal_pos = [(lb[i] + ub[i]) // 2 for i in range(len(lb))]
        self.min_distance = 10
        self.max_velocity = 40
        self.__zero = [0 for _ in range(len(lb))]

    def set_on_update(self, callback):
        self.__on_update = callback
    
    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def __distance(self, p1, p2):
        dist = 0
        for dim in range(self.dim):
            dist += (p2[dim] - p1[dim])**2

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
        separation = [0 for _ in range(self.dim)]

        for b in self.boids:
            if b != boid and self.__distance(boid.position, b.position) < self.min_distance:
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

    def __goal(self, boid):
        coef = .3
        result = [0 for _ in range(self.dim)]
        for dim in range(self.dim):
            result[dim] = (self.goal_pos[dim] - boid.position[dim]) * coef

        return result

    def __dodge(self, boid):
        coef = 1.1
        min_dist = self.min_distance * 3

        result = [0 for _ in range(self.dim)]
        closest = [boid.position[0], boid.position[1]]
        closest_dist = self.ub[0]
        for obstacle in self.obstacles:
            dist = self.__distance(boid.position, obstacle)
            if dist < min_dist and dist < closest_dist:
                closest_dist = dist
                closest = obstacle

        for dim in range(self.dim):
            result[dim] = -(closest[dim] - boid.position[dim]) * coef

        return result


    def __bounding_box(self, boid):
        coef = 1
        result = [0 for _ in range(self.dim)]
        for dim in range(self.dim):
            if boid.position[dim] < self.lb[dim]:
                result[dim] = self.min_distance * coef
            elif boid.position[dim] > self.ub[dim]:
                result[dim] = -self.min_distance * coef

        return result

    def update(self):
        for boid in self.boids:
            cohesion = self.__cohesion(boid) if self.cohesion else self.__zero
            separation = self.__separation(boid) if self.separation else self.__zero
            alignment = self.__alignment(boid) if self.alignment else self.__zero
            goal = self.__goal(boid) if self.goal else self.__zero
            dodge = self.__dodge(boid) if self.dodge else self.__zero
            bounding_box = self.__bounding_box(boid)

            for dim in range(self.dim):
                boid.velocity[dim] = cohesion[dim] + separation[dim] + alignment[dim] + goal[dim] + dodge[dim] + bounding_box[dim]
                if abs(boid.velocity[dim]) > self.max_velocity:
                    boid.velocity[dim] = boid.velocity[dim] / abs(boid.velocity[dim]) * self.max_velocity
                boid.position[dim] += boid.velocity[dim]

            if callable(self.__on_update):
                self.__on_update(self.boids)

    def run(self, iters):
        if iters:
            for _ in range(iters):
                self.update()
        else:
            while True:
                self.update()
    
if __name__ == '__main__':
    pass