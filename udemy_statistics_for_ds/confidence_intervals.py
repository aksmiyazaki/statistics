import pandas as pd
import math
from scipy import stats
import numpy as np
import scipy

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

df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/311.csv')

# There's no population variance and only a few observations, use t statistic to calculate CI.
mean = df['Values'].mean()
n = df['Values'].count()
## Two ways to calculate sample SE.
se = df['Values'].std() / math.sqrt(n)
se = scipy.stats.sem(df['Values'])
ci = [mean - (se * stats.t.ppf(1 - (0.01/2), (n-1))), mean + (se * stats.t.ppf(1 - (0.01/2), (n-1)))]

ci


# 2 Populations - Dependant.
df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/313.csv', sep=';')
xbar = df['Difference'].mean()
std = df['Difference'].std()

# With only 10 observations and population variance unknown, we need to use t-statistic.
# Also we have to assume that population is normally distributed.


se = std / (math.sqrt(df.count()[0])) ## Canculating by the formula
se = scipy.stats.sem(df['Difference']) ## Calculating using scipy
# With 95% ci, it means that alpha is 5% or 0.05, divided by 2 we have 0.025
tstat = stats.t.ppf((1-(0.05/2)), (df.count()[0] - 1))
ci = [xbar - (tstat * se), xbar + (tstat * se)]
ci

# With 95% of confidence we can say that the diet for 12 weeks makes people lose btw 11 and 6 kg.

## 2 Populations - Independant With population variance known
df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/314.csv', sep=';')

## 99% CI
## Z-statistic for 99% -> alpha = 1% or 0.01, divided by 2 -> alpha = 0.005
zstat = stats.norm.ppf(1 - (0.01/2))
var1 = df.loc['Population std','Engineering'] ** 2
var2 = df.loc['Population std','Management'] ** 2
n1 = df.loc['Size', 'Engineering']
n2 = df.loc['Size', 'Management']
se = math.sqrt(var1/n1 + var2/n2)

diff_mean = float(df.loc['Sample mean', 'Difference'])

ci = [diff_mean - (zstat * se), diff_mean + (zstat * se)]
ci

## The interval is bigger because our confidence is higher
## To give a better confidence we enlarge the interval because there's more chance that our value falls into a bigger interval.


## 2 Populations, variance unknown but assumed to be equal.
df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/315.csv', sep=';')
ny_mean = df['NYapples'].mean()
la_mean = df['LAapples'].mean()
ny_std = df['NYapples'].std()
la_std = df['LAapples'].std()

pool_var = (((df['NYapples'].count() - 1) * (ny_std ** 2))+ ((df['LAapples'].count() - 1) * (la_std ** 2))) / (df['LAapples'].count() + df['NYapples'].count() - 2)
pool_std = math.sqrt(pool_var)

# Unkown variance and only a few observations -> T-statistic.
tstat = stats.t.ppf((1-(0.1/2)), (df['NYapples'].count() + df['LAapples'].count() - 2))
tstat

ci = [(ny_mean - la_mean) - tstat * math.sqrt(pool_var/df['NYapples'].count() + pool_var/df['LAapples'].count()),
        (ny_mean - la_mean) + tstat * math.sqrt(pool_var/df['NYapples'].count() + pool_var/df['LAapples'].count())]
ci

## Confidence intervals for two means with independent variance -> Verify later.
