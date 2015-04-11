import numpy as np 
import pandas as pd
from numpy.linalg import inv

df_price = pd.read_csv('indeces-jul26-aug9-2012.csv')
del df_price['Date']
df_rets = np.log(df_price.shift(-1) / df_price)
df_rets = df_rets.drop(df_rets.index[-1])
#df_rets.to_csv('output.csv', sep=',')

df_norm = df_rets - df_rets.mean()
N = df_norm.shape[0]
mat_norm = np.matrix(df_norm)
mat_cov = np.round(1.0/(N-1) * mat_norm.transpose() * mat_norm,9)
pd.DataFrame(mat_cov,columns=df_rets.columns,index=df_rets.columns).to_csv('output.csv', sep=',')
