import pandas as pd
import numpy as np
from numpy.linalg import *


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
	print df_rets.head(10)
	df_norm = df_rets - df_rets.mean()
	N = df_norm.shape[0]
	mat_norm = np.matrix(df_norm)
	mat_cov = 1.0/(N-1) * mat_norm.transpose() * mat_norm
	mat_corr = corr_given_cov(mat_cov)
	return mat_cov, mat_corr

filename = 'data-DJ30-july2011-june2013-monthly.csv'
mat_cov, mat_corr = corr_and_cov_of_percent_ret_given_file(filename, b_log=True)
print np.round(mat_cov,6)
print np.round(mat_corr,6)