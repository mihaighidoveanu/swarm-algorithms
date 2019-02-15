from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

from pso import Swarm
from functions import *

class Plotter(object):

	# def __init__(self, arg):
		
	def plotPso(agentPozByEpoch,agentEvalsByEpoch,particleRange):
		# preconditions
		assert (isinstance(particleRange,tuple))
		# variables
		(minRange,maxRange) = particleRange
		# instantiate figure
		fig = plt.figure()
		ax = fig.gca(projection = '3d')
		plt.ion()
		# compute the plot surface (evaluation of func over the whole domain)
		Xgrid = np.arange(minRange,maxRange,0.01)
		Ygrid = np.arange(minRange,maxRange,0.01)
		Xgrid, Ygrid = np.meshgrid(Xgrid,Ygrid)
		Zvalue = applyToMeshgrid(Rossenbrock,Xgrid,Ygrid)
		# Plot the surface.
		surf = ax.plot_surface(Xgrid,Ygrid,Zvalue,cmap=cm.coolwarm,linewidth=0, antialiased=False)
		# Add a color bar which maps values to colors.
		fig.colorbar(surf, shrink=0.5, aspect=5)
		# for all the epochs, scatter plot particles positions and their evaluation
		for epoch in range(0,len(agentPozByEpoch)):
			agentPozX = [ agentPozByEpoch[epoch][nrAgent][0] for nrAgent in range(0,len(agentPozByEpoch[epoch])) ]
			agentPozY = [ agentPozByEpoch[epoch][nrAgent][1] for nrAgent in range(0,len(agentPozByEpoch[epoch])) ]
			# Scatter plot the particles
			agentEval = agentEvalsByEpoch[epoch]
			ax.scatter(agentPozX,agentPozY,agentEval, marker = '+')
		# return the figure with the plot
			plt.show()
			plt.pause(2)

		return fig 

	def plotParticles(agentPozByEpoch,agentEvalsByEpoch,particleRange):
		# preconditions
		assert (isinstance(particleRange,tuple))
		# variables
		(minRange,maxRange) = particleRange
		# instantiate figure
		fig = plt.figure()
		ax = fig.gca(projection = '3d')
		# for all the epochs, scatter plot particles positions and their evaluation
		for epoch in range(0,len(agentPozByEpoch)):
			agentPozX = [ agentPozByEpoch[epoch][nrAgent][0] for nrAgent in range(0,len(agentPozByEpoch[epoch])) ]
			agentPozY = [ agentPozByEpoch[epoch][nrAgent][1] for nrAgent in range(0,len(agentPozByEpoch[epoch])) ]
			ax.scatter(agentPozX,agentPozY,epoch, marker = '*')

		plt.show()
		plt.pause(100)
	




swarm = Swarm(20)
gb, Xs, Ys = swarm.pso((-3,3),Rossenbrock)
fig = Plotter.plotPso(Xs,Ys,(-3,3))
# Plotter.plotParticles(Xs,Ys,(-3,3))

