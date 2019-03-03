import pandas as pd

df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/27.csv', sep=';')
df['Annual income'] = df['Annual income'].astype(float)

df['Annual income'].mean()
df['Annual income'].median()
df['Annual income'].mode()

# Analysis: Definitely there's outliers because the mean is too far away from median and mode
# The most common used measure of central tendency in terms of income is median
