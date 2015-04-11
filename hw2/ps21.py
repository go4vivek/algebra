import numpy as np 
import pandas as pd
from numpy.linalg import *


#1
df_data = pd.read_csv("ps21.csv")

ls_ones = list(np.ones(15))
ls_2year = list(df_data['2-year'].values)
ls_3year = list(df_data['3-year'].values)
ls_5year = list(df_data['5-year'].values)
ls_10year = list(df_data['10-year'].values)

mat_y = np.matrix(ls_3year).transpose()
mat_A = np.matrix([ls_ones,ls_2year,ls_5year,ls_10year]).transpose()

mat_x = inv(mat_A.transpose()*mat_A) * mat_A.transpose() * mat_y
error1 = sum(np.array(mat_A*mat_x-mat_y)**2)**(0.5)


#2
error2 = sum( (np.array(ls_3year) - np.array(ls_2year)*2./3 - np.array(ls_5year)*1./3)**2)**(0.5)
#print error2

#3
date = np.array([2., 5., 10.])
r = [np.mean(np.array(df_data['2-year'].values)), np.mean(np.array(df_data['5-year'].values)), np.mean(np.array(df_data['10-year'].values))]
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
print np.round(cubic,6)