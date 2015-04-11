import numpy as np
from numpy.linalg import *
from math import *
import pandas as pd

disc = np.array([99.80, 99.35, 98.20, 97.75, 96.20])/100
date = [0./12, 1./12, 4./12, 10./12, 14./12, 20./12]
r = [0.75/100]
for i in range(1,6):
	r.append(-log(disc[i-1])/date[i])
#print np.array(r)

n = len(r)-1
b = np.zeros(shape=(4*n,1))
for i in range(1,n+1):
	b[4*i-3][0] = r[i-1]
	b[4*i-2][0] = r[i]
b = np.matrix(b)
#print np.round(b,6)

M = np.zeros(shape=(4*n,4*n))
M[0][2], M[0][3] = 2, 6*date[0]
M[-1][-2], M[-1][-1] = 2, 6*date[-1]
for i in range(1,n+1):
	M[4*i-3][4*i-4], M[4*i-3][4*i-3] = 1, date[i-1]
	M[4*i-3][4*i-2], M[4*i-3][4*i-1] = date[i-1]**2, date[i-1]**3
	M[4*i-2][4*i-4], M[4*i-2][4*i-3] = 1, date[i]
	M[4*i-2][4*i-2], M[4*i-2][4*i-1] = date[i]**2, date[i]**3
for i in range(1,n):
	M[4*i-1][4*i-3], M[4*i-1][4*i-2] = 1, 2*date[i]
	M[4*i-1][4*i-1], M[4*i-1][4*i+1] = 3*date[i]**2, -1
	M[4*i-1][4*i+2], M[4*i-1][4*i+3] = -2*date[i], -3*date[i]**2
	M[4*i][4*i-2], M[4*i][4*i-1] = 2, 6*date[i]
	M[4*i][4*i+2], M[4*i][4*i+3] = -2, -6*date[i]
M = np.matrix(M)

#print np.round(M,2)
#exit()
x = np.array(inv(M)*b)
np.savetxt("foo.csv", x, delimiter=",")
#print np.round(x,6)

date_new = [1./12,7./12,13./12,19./12]
r = []
for i in range(len(date_new)):
	r.append(x[4*i]+x[4*i+1]*date_new[i]+x[4*i+2]*date_new[i]**2+x[4*i+3]*date_new[i]**3)
disc = []
for i in range(len(r)):
	disc.append(exp(-r[i]*date_new[i]))

cash_flow = [2.5/2 for i in range(4)]
cash_flow[-1] += 100
print cash_flow

value = 0.
for i in range(4):
	#print cash_flow[i] * disc[i]
	value += cash_flow[i] * disc[i]
print np.round(value,6)
