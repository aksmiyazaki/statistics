import pandas as pd

df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/29.csv')

df.mean()

# Sample Variance
df['Annual Income'].var()

# This number tells that there's large distance between some points and the mean.

((1-3)**2 + (5-3) ** 2)/2
