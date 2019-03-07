import pandas as pd
import seaborn as sns

# It is a Sample
# COV Below.
df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/211.csv', sep=';')
df.cov()

# Scatter plot
sns.scatterplot(x='Writing', y='Reading', data=df)

# There is a noticeable relationship btw the two variables (when Writing is high, reading is high too).

df.corr()

# The correlation is almost perfect (almost 1), which implies that the correlation is very strong.
