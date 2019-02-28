import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set(style="whitegrid")
%matplotlib inline

interval_no = 6

df = pd.read_csv("/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/24-numericalvariables.csv")
interval =  np.ceil((df['Numbers'].max() - df['Numbers'].min()) / interval_no)

root = df['Numbers'].min() - 1
df_new = pd.DataFrame(columns=["Minimum", "Maximum"])
iter = 0

while root < df['Numbers'].max():
    df_new.loc[iter] = [root, root + interval]
    root += interval
    iter += 1

df_new["Frequency"] = 0

for iter, val in df.iterrows():
    df_new.loc[(val['Numbers'] > df_new['Minimum']) &
        (val['Numbers'] <= df_new['Maximum']), 'Frequency'] += 1

df_new["RelativeFreq"] = 0

for iter, val in df_new.iterrows():
    df_new.loc[iter, 'RelativeFreq'] = (val['Frequency'] / df_new['Frequency'].sum()) * 100

df_new

interval =  (df['Numbers'].max() - df['Numbers'].min()) / interval_no

root = df['Numbers'].min() - 1
df_new = pd.DataFrame(columns=["Minimum", "Maximum"])
iter = 0

while root < df['Numbers'].max():
    df_new.loc[iter] = [root, root + interval]
    root += interval
    iter += 1

df_new["Frequency"] = 0

for iter, val in df.iterrows():
    df_new.loc[(val['Numbers'] > df_new['Minimum']) &
        (val['Numbers'] <= df_new['Maximum']), 'Frequency'] += 1

df_new["RelativeFreq"] = 0

for iter, val in df_new.iterrows():
    df_new.loc[iter, 'RelativeFreq'] = (val['Frequency'] / df_new['Frequency'].sum()) * 100

df_new
