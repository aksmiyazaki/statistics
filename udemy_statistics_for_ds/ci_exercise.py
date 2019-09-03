import pandas as pd
import math
from scipy import stats
import numpy as np
import scipy

df_2015 = pd.read_csv("/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/317_2015.csv", sep=';')
df_2016 = pd.read_csv("/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/317_2016.csv", sep=';')

df_2015.set_index('US', inplace=True)
df_2016.set_index('US', inplace=True)

df_2015.columns = pd.MultiIndex.from_product([['2015'], df_2015.columns])
df_2016.columns = pd.MultiIndex.from_product([['2016'], df_2016.columns])
df = pd.concat([df_2015, df_2016], axis=1)


df.columns = df.columns.droplevel()
df.mean(axis=1)

# SE = VAR / sqrt(n)
df.var(axis=1) / math.sqrt(len(df.columns))

# We are using t-statistic with 95% CI
# then, alpha = 0,05 or 5%, alpha/2 = 0,025
# 1 - 0,025 = 0.975
cv = stats.t.ppf(1 - (0.05/2), (len(df.columns)-1))
cv

df.var(axis=1) / math.sqrt(len(df.columns)) * cv
