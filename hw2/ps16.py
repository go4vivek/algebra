import scipy.stats as st
from math import *
import numpy as np

print np.round(st.norm.ppf(.95)/st.norm.ppf(.99)*10,6)
print np.round(st.norm.ppf(.95)*sqrt(5)/st.norm.ppf(.99)/sqrt(2)*10,6)