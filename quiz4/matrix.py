import numpy as np 

a = np.matrix([[-1,3],[2,1]])
b = np.matrix([[1,0],[0,-2]])
print a*b*np.linalg.inv(a)*np.matrix([2,-3]).transpose()