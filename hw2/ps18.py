import numpy as np 
from numpy.linalg import *
from math import *
from scipy.optimize import newton
import pandas as pd
from scipy.linalg import *
import scipy.stats as st
from scipy.stats import norm

def cov_given_corr(mat_corr, na_std):
	mat_D = np.diag(na_std);
	mat_cov = mat_D*mat_corr*mat_D
	return mat_cov

mat_corr = np.matrix([[1,-0.25,0.5],[-0.25,1,0.25],[0.5,0.25,1]])
na_std = [0.15,0.2,0.25]
Sigma = cov_given_corr(mat_corr,na_std)

mu = np.matrix([0.05,0.09,0.1]).transpose()
mu_P = 0.08
r_f = 0.02
mu_bar = mu - r_f
x = inv(Sigma)*mu_bar
w = x*(mu_P - r_f)/(mu_bar.transpose()*x)

mu_R = r_f + mu_bar.transpose()*w
w_cash = 1.0 - np.matrix(np.ones((1,3)))*w
sigma = sqrt(w.transpose()*Sigma*w)
sharpe = (mu_R-r_f)/sigma
#print w.transpose(), w_cash, mu_R, sigma, sharpe


w = np.matrix([1./3,1./3,1./3]).transpose()
mu_Y = float(r_f + mu_bar.transpose()*w)
#print mu_Y
Sigma_Y = float(w.transpose()*Sigma*w)
print norm.cdf((0.09-mu_Y)/sqrt(Sigma_Y))-norm.cdf((0.07-mu_Y)/sqrt(Sigma_Y))