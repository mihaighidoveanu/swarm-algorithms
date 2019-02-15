import math

def Rosenbrock(input):
    x, y = input
    return 100*((input[1]-input[0]**2)**2+(1-input[0])**2)

def Rastrigin (input):
    return 20 + (input[0]**2 - 10*math.cos(2*math.pi*input[0])) + input[1]**2 - 10*math.cos(2*math.pi*input[1])

def Griewank(input):
    return (input[0]**2 + input[1]**2)/4000 - (math.cos(input[0]))*(math.cos(input[1]/math.sqrt(2))) + 1