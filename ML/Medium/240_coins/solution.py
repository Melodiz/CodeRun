import pandas as pd
data = pd.read_csv('coins.in',sep=' ',header=None).rename({0:'n',1:'k'},axis=1)

data['new_col'] = data[1]/data[0]
data.k = data.k+1
data.n = data.n+2
data['new_col'] = data.k/data.n
data = data.sort_values('new_col').reset_index()
data['index'].to_csv('output.txt',index=None,sep=' ')