import numpy as np
import pandas as pd 
from math import *
from numpy.linalg import *
from scipy.stats import norm
from scipy.optimize import newton

w

ls_ones = list(np.ones(18))
ls_strikes = list(-df_data['strike'].values)
mat_A = np.matrix([ls_ones,ls_strikes]).transpose()
#print mat_A

ls_call = list((df_data["bid price call"].values+df_data["ask price call"].values)/2)
ls_put = list((df_data["bid price put"].values+df_data["ask price put"].values)/2)
mat_C = np.matrix([ls_call]).transpose()
mat_P = np.matrix([ls_put]).transpose()
#print mat_C, mat_P

mat_y = mat_C - mat_P
mat_x = inv(mat_A.transpose()*mat_A)*mat_A.transpose()*mat_y
#print np.round(mat_x,6)

def fc(x, K, C):
	global mat_x
	f_PVF,f_disc = float(mat_x[0][0]), float(mat_x[1][0])
	T = 240./365
	d1 = log(f_PVF/K/f_disc)/(x*sqrt(T)) + x*sqrt(T)/2
	d2 = log(f_PVF/K/f_disc)/(x*sqrt(T)) - x*sqrt(T)/2
	return f_PVF*norm.cdf(d1) - K*f_disc*norm.cdf(d2) - C

def fp(x, K, P):
	global mat_x
	f_PVF,f_disc = float(mat_x[0][0]), float(mat_x[1][0])
	T = 240./365
	d1 = log(f_PVF/K/f_disc)/(x*sqrt(T)) + x*sqrt(T)/2
	d2 = log(f_PVF/K/f_disc)/(x*sqrt(T)) - x*sqrt(T)/2
	return -f_PVF*norm.cdf(-d1) + K*f_disc*norm.cdf(-d2) - P

def fprimec(x, K, C):
	global mat_x
	f_PVF,f_disc = float(mat_x[0][0]), float(mat_x[1][0])
	T = 240./365
	d1 = log(f_PVF/K/f_disc)/(x*sqrt(T)) + x*sqrt(T)/2
	return f_PVF*sqrt(T/2/pi)*exp(-d1**2/2)

def fprimep(x, K, P):
	global mat_x
	f_PVF,f_disc = float(mat_x[0][0]), float(mat_x[1][0])
	T = 240./365
	d1 = log(f_PVF/K/f_disc)/(x*sqrt(T)) + x*sqrt(T)/2
	return f_PVF*sqrt(T/2/pi)*exp(-d1**2/2)

print "Strike", "\t", "Imp_Vol(call)", "\t", "Imp_Vol(put)"
for i in range(df_data.shape[0]):
	K = -ls_strikes[i]
	C = ls_call[i]
	P = ls_put[i]
	print K, "\t", round(newton(fc,0.25,fprimec,args=(K,C), tol=1.48e-10),6), "\t", round(newton(fp,0.25,fprimep,args=(K,P), tol=1.48e-10),6)