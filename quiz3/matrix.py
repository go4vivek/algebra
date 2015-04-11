import numpy as np 

#A = np.matrix([[1,0.2,-0.2,0.1],[0.2,1,-0.25,0.05],[-0.2,-0.25,1,-0.15],[0.1,0.05,-0.15,1]])
#print np.linalg.det(A)

A = np.matrix([[1,0.1,0.2],[0.1,1,-0.3],[0.2,-0.3,1]])
print np.linalg.cholesky(A).transpose()