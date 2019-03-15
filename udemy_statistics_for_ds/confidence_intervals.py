import pandas as pd
import math
from scipy import stats

population_std = 15000
df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/39.csv')
df.count()
standard_err = population_std / math.sqrt(df.count())
# alpha = 10% or 0.1
# alpha/2 = 0.05
# 1 - 0.05 = 0.95
# Then, Z = 1.65
zalphad2 = stats.norm.ppf(0.95)
[df['Values'].mean() - (zalphad2 * standard_err), df['Values'].mean() + (zalphad2 * standard_err)]

## TASK -> See more ways to calculate the CI.
