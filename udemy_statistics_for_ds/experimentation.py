import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def create_frequency_table(df, aim_col, interval_no, must_round = True, minValue = None, maxValue = None):
    if minValue == None:
        root = df[aim_col].min()
    else:
        root = minValue

    if maxValue == None:
        top = df[aim_col].max()
    else:
        top = maxValue

    interval =  (top - root) / interval_no
    if must_round:
        interval = np.ceil(interval)

    df_new = pd.DataFrame(columns=["Minimum", "Maximum"])
    iter = 0
    while root < top:
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

df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/213.csv', sep=';')
df['Price'] = df['Price'].apply(lambda x: x[x.index('$') + 1:].replace(',','')).astype(float)

# Cust ID - Categorical, Qualitative Nominal
# Mortgage - Categorical, Qualitative Nominal
# Year of Sale - Numerical Discrete, Quantitative Interval
interval_no=272
fq_table = create_frequency_table(df, 'Price', interval_no, must_round = True)

interval = np.ceil((df['Price'].max() - df['Price'].min()) / interval_no)
sns.distplot(df['Price'], bins=interval_no, kde=False)

interval_no=5
n, bins, patches = plt.hist(x=df['Price'], bins=[0, 100000, 200000, 300000, 400000, 500000, 600000], range=(0,600000))

df['Price'].skew()

# The mode of Prices is between 200k and 300k
# Also, the skew is Positive, which means that it's more common to have a lower value (until 400k)
# Than a higher value (> 400k)
sns.scatterplot(x=df['Price'], y=df['Area (ft.)'])

df[['Price','Area (ft.)']].corr()
# There is a clear relationship between the two variables.
# We can see the strong relationship in correlation (0.95, pretty near the perfect correlation)
fq_table = pd.DataFrame()
fq_table['Frequency'] = df[df['Status'] == 'Sold']['Country'].value_counts()
fq_table['RelativeFrequency'] = 0
fq_table['RelativeFrequencySum'] = 0

for iter, row in fq_table.iterrows():
    fq_table.loc[iter, 'RelativeFrequency'] = (row['Frequency'] / fq_table['Frequency'].sum()) * 100

iter = 0
for it, row in fq_table.iterrows():
    value = row['RelativeFrequency']
    for x in range(0, iter):
        value += fq_table.iloc[x]['RelativeFrequency']

    fq_table.loc[it, 'RelativeFrequencySum'] = value
    iter += 1

fq_table

# Creation of pareto diagram with seaborn
sns.set_style("white")
fig, ax = plt.subplots()
ax = sns.barplot(x=fq_table.index, y=fq_table['Frequency'])
ax2 = ax.twinx()
ax2 = sns.pointplot(x=fq_table.index, y=fq_table['RelativeFrequencySum'], order=["USA", "Canada", "Russia", "UK", "Belgium", "Denmark", "Germany", "Mexico"], color="Y")
plt.ylim(0,100)
sns.despine(ax=ax, right=True, left=True)
sns.despine(ax=ax2, left=True, right=False)
ax2.spines['right'].set_color('white')

df['Price'].mean()
df['Price'].median()
df['Price'].mode()
df['Price'].skew()
df['Price'].var()
df['Price'].std()

# The Skew is positive, so the ouliers are the highest prices (we can see that because the Mean is higher than the median)
# The prices usually vary at most 90k from the mean
df[['Price','Area (ft.)']].cov()
df[['Price','Area (ft.)']].corr()
# As I've said before, the correlation is very strong between those two variables.
