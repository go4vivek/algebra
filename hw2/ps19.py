import numpy as np
from numpy.linalg import *
from math import *
import scipy.stats as st

def cov_given_corr(mat_corr, na_std):
	mat_D = np.diag(na_std);
	mat_cov = mat_D*mat_corr*mat_D
	return mat_cov

def VaR(N,C,sigma,mu,v):
	return (sqrt(float(N)/252)*sigma*st.norm.ppf(C)-float(N)/252*mu)*v

'''
#1
na_mu = [0.08,0.12,0.16]
na_sigma = np.array([.25,.25,.3])
for i in range(3):
	print VaR(5.,.95,na_sigma[i],na_mu[i],100.)
'''

#3
na_mu = [0.08, 0.16]
mat_corr = np.matrix([[1, 0.25],[0.25,1]])
na_std = np.array([0.25, 0.30])
cov = cov_given_corr(mat_corr,na_std)
sigma = 1/ sqrt(np.matrix(np.ones((1,len(na_std))))*inv(cov)*np.matrix(np.ones((len(na_std),1))))
w = inv(cov)*np.matrix(np.ones((len(na_std),1)))/(np.matrix(np.ones((1,len(na_std))))*inv(cov)*np.matrix(np.ones((len(na_std),1))))
mu = float(na_mu*w)
print sigma,VaR(5.,.95,sigma,mu,100.)



