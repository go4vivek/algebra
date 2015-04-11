import numpy as np 
from numpy.linalg import *
from math import *
from scipy.optimize import newton
import pandas as pd
from scipy.linalg import *
import scipy.stats as st
from scipy.stats import norm





'''
A = np.matrix([[0.25,-0.5,1.5],[1,-1,1.25],[-0.5,-0.25,2],[0,0.5,0.75],[-1,0.75,1.5]])
A = pd.DataFrame(A)
A = A - A.mean()
A = np.matrix(A)
cov = 1.0/(5-1) * A.transpose() * A
print cov


def determinant(rho):
	A = np.matrix([[1.,rho,0.2],[rho,1,-0.1],[0.2,-0.1,1]])
	return det(A)

print newton(determinant,-1)


A = np.matrix([[4,3,-0.3],[3,4,-0.2],[-0.3,-0.2,1]])
print cholesky(A)


M = np.matrix([[exp(0.015),exp(0.015)],[60,45]])
s = np.matrix([0,5])
Theta = s * inv(M)
print Theta
'''