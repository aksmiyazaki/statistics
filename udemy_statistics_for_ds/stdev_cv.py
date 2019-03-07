import pandas as pd

df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/210.csv', sep=';')
df
# Obviously, this is a sample, so we are using sample formulas.

df['Annual income USA'].mean()
df['Annual income USA'].var()

df['Annual income Denmark'].mean()
df['Annual income Denmark'].var()

# Calculate STD of both
df['Annual income USA'].std()
df['Annual income Denmark'].std()

# Calculate coefficient of variation
df['Annual income USA'].std()/df['Annual income USA'].mean()
df['Annual income Denmark'].std()/df['Annual income Denmark'].mean()

# This means that annual income in USA has a huge variability compared with annual incomes in denmark.
