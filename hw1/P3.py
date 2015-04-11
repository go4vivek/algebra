'''
import numpy as np
import scipy as sp

B = np.matrix([[0,0,0,0],[3,0,0,0],[1,-1,0,0],[-1,2,1,0]])
C = np.matrix([[1,0,0,0],[3,1,0,0],[1,-1,1,0],[-1,2,1,1]])
print sp.linalg.lu(C)
'''
import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

A = scipy.array([ [7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
P, L, U = scipy.linalg.lu(A)

print "A:"
pprint.pprint(A)
print "P:"
pprint.pprint(P)

print "L:"
pprint.pprint(L)

print "U:"
pprint.pprint(U)