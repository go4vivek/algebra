import numpy as np 
from numpy.linalg import inv
import pandas as pd
from numpy.linalg import eig
from scipy.linalg import sqrtm
from numpy.linalg import cholesky
from math import *

def corr_given_cov(mat_cov):
	mat_D = np.diag(np.sqrt(np.diag(mat_cov)))
	mat_corr = inv(mat_D) * mat_cov * inv(mat_D)
	return mat_corr

def cov_given_corr(mat_corr, na_std):
	mat_D = np.diag(na_std);
	mat_cov = mat_D*mat_corr*mat_D
	return mat_cov

def corr_and_cov_of_percent_ret_given_file(filename='indices-july2011.csv', delta_time=1, b_log=False):
	df_price = pd.read_csv(filename)
	del df_price['Date']
	if b_log == False:
		df_rets = df_price.shift(-delta_time) / df_price - 1
	else:
		df_rets = np.log(df_price.shift(-delta_time) / df_price)
	if delta_time > 1:
		df_rets = df_rets.drop(df_rets.index[-delta_time:-1])
	df_rets = df_rets.drop(df_rets.index[-1])
	df_norm = df_rets - df_rets.mean()
	N = df_norm.shape[0]
	mat_norm = np.matrix(df_norm)
	mat_cov = 1.0/(N-1) * mat_norm.transpose() * mat_norm
	mat_corr = corr_given_cov(mat_cov)
	return mat_cov, mat_corr

filename = 'indices-july2011.csv'
mat_cov, mat_corr = corr_and_cov_of_percent_ret_given_file(filename=filename, delta_time=1, b_log=False)

print np.round(mat_cov*10e5,3)
print np.round(mat_corr,3)

'''
na_vector = np.zeros(shape=(4,4))
for i in range(4):
	for j in range(4):
		na_vector[i][j] = sin((i+1.)*(j+1.)*pi/5)
print "Eigenvectors:"
print na_vector

print "Of norm 1?"
for i in range(4):
	print sum(na_vector[i]*na_vector[i])

print "Orthogonal?"
for i in range(4):
	for j in range(i+1,4):
		print sum(na_vector[i]*na_vector[j])

mat_A = np.matrix([[2,-2],[-2,5]])
mat_M = cholesky(mat_A)
print mat_M

print mat_M*mat_M.transpose()



mat_A = np.matrix([[2,0,0],[10,2,0],[0,10,2]])
print eig(mat_A)



filename = 'indices-july2011.csv'
mat_cov, mat_corr = corr_and_cov_of_percent_ret_given_file(filename=filename, delta_time=21, b_log=True)

print np.round(mat_cov*10e6,3)
print np.round(mat_corr,3)


mat_corr = np.matrix([[1,-0.25,0.15,-0.05,-0.30],\
	[-0.25, 1, -0.10, -0.25, 0.10],\
	[0.15, -0.10, 1, 0.20, 0.05],\
	[-0.05, -0.25, 0.20, 1, -0.10],
	[-0.30, 0.10, 0.05, -0.10, 1]])
na_std = np.array([4, 2, 1, 0.5, 0.25])
print cov_given_corr(mat_corr, na_std)
'''