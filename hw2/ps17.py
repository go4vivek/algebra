import numpy as np
from math import *
from numpy.linalg import *

Sigma = np.matrix([[0.09,0.01,0.03,-0.015],[0.01, 0.0625, -0.02, -0.01],[0.03,-0.02,0.1225,0.02],[-0.015,-0.01,0.02,0.0576]])
mu = np.matrix([0.04,0.035,0.05,0.034]).transpose()
r_f = 0.01
mu_bar = mu - r_f

x = inv(Sigma)*mu_bar
#x = inv(Sigma)*np.matrix(np.ones((4,1)))
w = x/(np.matrix(np.ones((1,4)))*x)

#mu_P = 0.03
#w = x*(mu_P - r_f)/(mu_bar.transpose()*x)

#sigma_P = 0.27
#w = x*sigma_P/sqrt(mu_bar.transpose()*x)

mu_R = r_f + mu_bar.transpose()*w
w_cash = 1.0 - np.matrix(np.ones((1,4)))*w
sigma = sqrt(w.transpose()*Sigma*w)
sharpe = (mu_R-r_f)/sigma
print w.transpose(), w_cash, mu_R, sigma, sharpe