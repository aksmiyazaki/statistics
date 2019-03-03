import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set(style="whitegrid")
%matplotlib inline

# Creating a crosstable using pandas.
df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/26.csv', sep=';')
pd.crosstab(df['Range'], df['Situation'], values=df['Percent'], aggfunc=sum, margins=True, margins_name="Total")

df

# Barplotting the crosstable with seaborn
sns.barplot(x='Range', y='Percent', hue='Situation', data=df)

trace1 = go.Bar(
    x=df[df['Situation'] == 'Employed']['Range'],
    y=df[df['Situation'] == 'Employed']['Percent'],
    name='Employed'
)
trace2 = go.Bar(
    x=df[df['Situation'] == 'Unemployed']['Range'],
    y=df[df['Situation'] == 'Unemployed']['Percent'],
    name='Unemployed'
)

layout = go.Layout(
    barmode='group'
)

# Barplotting the crosstable with Plotly
py.iplot([trace1, trace2], layout=layout)


df = pd.read_csv('/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/26_2.csv', sep=';')
df.head()

# Scatterplotting data with seaborn
sns.scatterplot(x='Apple (AAPL)', y='Alphabet (GOOGL)', data=df)

# Scatterplotting data with Plotly
trace = go.Scatter(
    x = df['Apple (AAPL)'],
    y = df['Alphabet (GOOGL)'],
    mode = 'markers'
)

py.iplot([trace])

# Plot Analysis: It seems the two variables are positive correlatedself.

# Scatterplotting data with Seaborn
sns.scatterplot(x='Apple (AAPL)', y='Bank of America (BAC)', data=df)

# Scatterplotting data with Plotly
trace = go.Scatter(
    x = df['Apple (AAPL)'],
    y = df['Bank of America (BAC)'],
    mode = 'markers'
)

py.iplot([trace])

# Analysis: Data doesn't seem to be correlated.
