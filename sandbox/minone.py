import numpy as np
import matplotlib.pyplot as plt
from ypstruct import structure
import genetic_algorithm

# Cost function - Sphere Test Function
def sphere(x):
    return sum(x**2)

# Problem Definition
problem = structure()
problem.costfunc = sphere
problem.nvar = 5
problem.varmin = -10
problem.varmax = 10

# GA Parameters
params = structure()
params.maxit = 100
params.npop = 20
params.pc = 1
params.gamma = 0.1
params.mu = 0.2 # como temos 5 genes (nvar), sempre vamos alterar 1 na mutacao
params.sigma = 0.1

# Run GA
out = genetic_algorithm.run(problem, params)

# Results

