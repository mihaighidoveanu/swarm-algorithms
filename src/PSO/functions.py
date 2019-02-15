import numpy as np
import math

# All functions are computed for a particle x with n = len(x) dimensions


# f : [-3,3]
def Rossenbrock(x):
    # convert the array to a numpy one
    x = np.asarray(x)
    #preconditions
    assert(len(x.shape) == 1)	#is an array
    assert(all(agent >= -3 and agent <= 3 for agent in x)) #has values in function domain
    # compute the function
    result = 0
    for i in range(0,len(x) - 1):
        result += 100 * (x[i + 1] - x[i]**2)**2 + (1 - x[i]**2)
    # finish
    return result

# f : [-5.12,5.12]
def Rastrigin(x):
    # convert the array to a numpy one
    x = np.asarray(x)
    # preconditions
    assert(len(x.shape) == 1)   #is an array
    assert(all(agent >= -5.12 and agent <= 5.12 for agent in x)) #has values in function domain
    # compute the function
    n = len(x)
    result = 10 * n
    for i in range(0,n):
        result += x[i]**2 - 10 * math.cos(2 * math.pi * x[i])
    # finish
    return result

# f : [-600,600]
def Griewank(x):
    # convert the array to a numpy one
    x = np.asarray(x)
    # preconditions
    assert(len(x.shape) == 1)   #is an array
    assert(all(agent >= -5.12 and agent <= 5.12 for agent in x)) #has values in function domain
    # compute the function
    result = 1
    for i in range(0,len(x)):
        result += x[i]**2 / 4000
        result -= math.cos(x[i] / math.sqrt(i + 1))
    # finish
    return result

# applies a function to meshgrid results X and Y
def applyToMeshgrid(func,X,Y):
    # preconditions
    assert (hasattr(func,'__call__'))
    # apply the function to each particle of the meshgrid ([ X[i][j] Y[i][j] ])
    Z = np.zeros(X.shape)
    for i in range(0,X.shape[0]):
        for j in range(0,X.shape[1]):
            Z[i][j] = func([ X[i][j], Y[i][j] ])
    # return the z values
    return Z

