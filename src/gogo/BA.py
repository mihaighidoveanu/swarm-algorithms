import random

class BA:
    def __init__(self, n=100, m=10, e=3, nep=40, nsp=20, ngh=.2):
        self.n = n        # number of scout bees
        self.m = m        # number of selected sites
        self.e = e        # number of best sites
        self.nep = nep    # number of bees recruited for best sites
        self.nsp = nsp    # number of bees recruited for remaining sites
        self.ngh = ngh    # initial size of patches

        self.__on_iter_handler = None


    def set_iter_handler(self, callback):
        self.__on_iter_handler = callback


    def run(self, iters, fitness, lb, ub):
        dim = len(lb)
        scouts = [[random.uniform(lb[i], ub[i]) for i in range(dim)] 
                    for _ in range(self.n)]

        for iter in range(iters):
            scouts.sort(key=lambda x: fitness(x), reverse=True)

            best = scouts[0:self.m]

            for i in range(len(best)):
                if i < self.e:
                    bee = sorted([[random.uniform(best[i][j] - self.ngh, best[i][j] + self.ngh) for j in range(dim)] 
                            for _ in range(self.nep)], key=lambda x: fitness(x), reverse=True)[0]
                else:
                    bee = sorted([[random.uniform(best[i][j] - self.ngh, best[i][j] + self.ngh) for j in range(dim)] 
                            for _ in range(self.nsp)], key=lambda x: fitness(x), reverse=True)[0]

                best[i] = bee

            scouts[self.m:] = [[random.uniform(lb[i], ub[i]) for i in range(dim)] 
                    for _ in range(self.n - self.m)]

            if callable(self.__on_iter_handler):
                self.__on_iter_handler(scouts, iter)

        return scouts[0]


if __name__ == '__main__':
    print(BA().run(100, lambda input: -(input[0]**2 + input[1]**2), [-10, -10], [10, 10]))