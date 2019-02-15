import numpy as np
from functions import Rossenbrock, Rastrigin, Griewank

class Swarm(object):
	"""class for dealing with swarms"""

	def __init__(self, nr_agents):
			self.nr_agents = nr_agents  
			self.inertia = 1
			self.socialWeight = 2
			self.personalWeight = 2

	# Particle Swarm Optimisation 
	# @func = function to minimize = f : D^n -> R
	# @particleRange = tuple representing the domain of @func = D
	# @numDimensions = the dimensions of function's domain = n
	# @returns (X,Y,Xs,Ys)
	# 	@X best position
	# 	@Y best position evaluation
	# 	@Xs all positions indexed by epochs
	# 	@Ys evaluations of all positions indexed by epochs
	def pso(self,particleRange,func,numDimensions = 2,maxIter = 100):
		#preconditions
		assert (isinstance(particleRange,tuple))
		assert (hasattr(func,'__call__'))

		# initialize variables
		minRange = particleRange[0]
		maxRange = particleRange[1]
		Xshape = (self.nr_agents,numDimensions)
		X = np.zeros(Xshape) #population of particles
		Xs = np.zeros((maxIter,self.nr_agents,numDimensions))
		Ys = np.zeros((maxIter,self.nr_agents))
		Y = np.zeros(Xshape) #current evaluation of particles
		pb = np.full(Xshape,maxRange) #personal bests of particles
		gb = np.full(numDimensions,maxRange) #global best of swarm
		velocities = np.zeros(Xshape) #velocities for each particle

		# create a population of agents in the specified range
		for i in range(0, len(X)):
			X[i] = np.random.uniform(minRange, maxRange,numDimensions)
			

		#loop until convergence
		epoch = 0
		while(True):
			# store particle's current position
			Xs[epoch] = X

			# evaluate each particle's current position according to the objective function
			Y = np.asarray([func(particle) for particle in X])
			Ys[epoch] = Y

			
			# for all the particles, 
			#update the personal bests for the ones where their current position is better then their previous best
			# the minimum of the personal bests will be the global best
			for i in range(0,len(pb)):
				pbCost = func(pb[i])
				gbCost = func(gb)
				if(Y[i] < pbCost):
					# print('Updated pb %d' %i) #debug
					pb[i] = X[i]
				if(pbCost < gbCost):
					# print('Updated gb %d' %i) #debug
					gb = X[i]	

			# update velocities of the particles
			rand1 = np.random.uniform(0,1)	#two random floats between 0 and 1 
			rand2 = np.random.uniform(0,1) 
			vPersonal = self.personalWeight * rand1 * (pb - X)
			vSocial = self.socialWeight * rand2 * (gb - X)
			velocities = self.inertia * velocities + vPersonal + vSocial
			
			# move particles to their new position, and take care that particles don't exceed particleRange
			X = X + velocities
			for i in range(0, len(X)):
				for dim in range(0, 2):
					if(X[i][dim] < minRange):
						X[i][dim] = minRange
					if(X[i][dim] > maxRange):
						X[i][dim] = maxRange

			# stop looping if following criteria is statisfied
			#stop if algorithm ran for more than max iterations
			epoch = epoch + 1
			if(epoch >= maxIter):
				break

			#if velocities become very small, the algorithm converges, so we stop it
			velocityConverge = [velocities[i][dim] <= 1 for dim in range(0,velocities.shape[1]) for i in range(0,velocities.shape[0])]
			if(all(velocityConverge)):
				break
			
			#debug code in loop
			# print("Epoch : %d" %epoch)
			# print(X)
			# print(Y)

		#debug code outside loop
		# print('Global best %d %d' %(gb[0], gb[1]))
		
		return (gb,Xs,Ys)
	

# main 
swarm = Swarm(20)
gb, Xs, Ys = swarm.pso((-3,3),Rossenbrock)
print(gb)
print(Rossenbrock(gb))
