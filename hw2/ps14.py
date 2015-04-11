import numpy as np
from numpy.linalg import *
from math import *
from decimal import *
from numpy.linalg import cholesky

A = np.matrix([[1.5,101.5,0,0],[2,2,102,0],[0,6,0,106],[2.5,2.5,2.5,102.5]])
print cholesky(A)
exit()



b = np.matrix([101.30,102.95,107.35,105.45]).transpose()
disc = (inv(A)*b)
#print disc

date = np.array([0., 4./12,10./12,16./12,22./12])
r = []
for i in range(1,5):
	r.append(-log(float(disc[i-1]))/date[i])
	if i == 1:
		r.append(r[0])
print np.round(np.array(r),9)
exit()

n = len(r)-1
b = np.zeros(shape=(4*n,1))
for i in range(1,n+1):
	b[4*i-3][0] = r[i-1]
	b[4*i-2][0] = r[i]
b = np.matrix(b)
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
cubic = np.array(inv(M)*b)
#print cubic

def f(x):
	global cubic
	if x <= 4./12:
		return cubic[0]+cubic[1]*x+cubic[2]*x**2+cubic[3]*x**3
	elif x <= 10./12:
		return cubic[4]+cubic[5]*x+cubic[6]*x**2+cubic[7]*x**3
	elif x <= 16./12:
		return cubic[8]+cubic[9]*x+cubic[10]*x**2+cubic[11]*x**3
	elif x <= 22./12:
		return cubic[12]+cubic[13]*x+cubic[14]*x**2+cubic[15]*x**3


date_new = np.array([2./12,5./12,8./12,11./12,14./12,17./12,20./12])
r = []
for i in range(len(date_new)):
	r.append(f(date_new[i]))
disc = []
for i in range(len(r)):
	disc.append(exp(-r[i]*date_new[i]))
print disc

cash_flow = [3.0/4 for i in range(7)]
cash_flow[-1] += 100
print cash_flow

value = 0.
for i in range(7):
	value += cash_flow[i] * disc[i]
print value