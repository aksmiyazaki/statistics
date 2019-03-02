import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set(style="whitegrid")
%matplotlib inline

def create_frequency_table(df, aim_col, interval_no, must_round = True):
    interval =  (df[aim_col].max() - df[aim_col].min()) / interval_no
    if must_round:
        interval = np.ceil(interval)


    root = df[aim_col].min()
    df_new = pd.DataFrame(columns=["Minimum", "Maximum"])

    iter = 0
    while root < df[aim_col].max():
        df_new.loc[iter] = [root, root + interval]
        root += interval
        iter += 1

    df_new["Frequency"] = 0
    root = df[aim_col].min()

    df[df[aim_col] == root].count()
    df_new.loc[0,"Frequency"] += 1

    for iter, val in df.iterrows():
        if val[aim_col] > root:
            df_new.loc[(val[aim_col] > df_new['Minimum']) &
                (val[aim_col] <= df_new['Maximum']), 'Frequency'] += 1

    df_new["RelativeFreq"] = 0

    for iter, val in df_new.iterrows():
        df_new.loc[iter, 'RelativeFreq'] = (val['Frequency'] /
            df_new['Frequency'].sum()) * 100

    return df_new


interval_no = 6
df = pd.read_csv("/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/24.csv")
df_new = create_frequency_table(df, "Numbers", interval_no)
df_new

df_new = create_frequency_table(df, "Numbers", interval_no, False)
df_new

## Starting exercise 2.5
interval_no = 10
df = pd.read_csv("/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/25.csv")
df_new = create_frequency_table(df, "Numbers", interval_no)
df_new['Range'] = df_new['Minimum'].astype(str) + "," + df_new['Maximum'].astype(str)

sns.distplot(df['Numbers'], bins=interval_no, kde=False)
interval = np.ceil((df['Numbers'].max() - df['Numbers'].min()) / interval_no)

data = [go.Histogram(x=df['Numbers'], xbins=dict(start=df['Numbers'].min(),
    end=df['Numbers'].max(), size=interval))]
py.iplot(data)
