import numpy as np 




#mat_M = np.matrix([[1,1,1,1],[32,38,42,44],[0,2,6,8],[8,2,0,0]])
#f_det_M = np.linalg.det(mat_M)
#print f_det_M


#mat_s = np.matrix([[0,4,6,6]])
#print mat_s*np.linalg.inv(mat_M)

#mat_S0 = np.matrix([[1,40,8,5]])
#print np.linalg.inv(mat_M)* mat_S0.transpose()

#mat_V = np.matrix([[0,1,0,0]])
#print mat_V * np.linalg.inv(mat_M)

A = np.matrix([[1,1,1],[1,1,1],[1,1,1]])
print A*A*A-3*A*A