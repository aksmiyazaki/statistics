import pandas as pd
import seaborn as sns
import numpy as np


df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/28.csv')
df2 = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/28_2.csv')

df['Values'].skew()
df.sort_values(by='Values', inplace=True)
sns.distplot(df['Values'], bins=20)



df2['Values'].skew()
df2.sort_values(by='Values', inplace=True)
sns.distplot(df2['Values'], bins=20)
