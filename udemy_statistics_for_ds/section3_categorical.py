import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
%matplotlib inline

df = pd.read_csv("/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/23-categoricalvariables.csv", sep='\t')

# First task - order data by frequency
df.sort_values(by='Sold', inplace=True)
df.set_index('City', inplace=True)
df.head()

# Then, plot a barplot with pandas
df.plot(kind='bar')

# Plotting with plotly
data = [go.Bar(x=df.index, y=df['Sold'])]
py.iplot(data)

# Plotting with Seaborn
ax = sns.barplot(x=df.index, y='Sold', data=df)


# Calculate relative values for items.
df['Relative'] = df['Sold'].apply(lambda x:x/df.sum())
df

# Plotting with pandas
df.plot(x='City', y='Relative', kind='pie')

# Plotting with plotly
data = go.Pie(labels=df.index, values=df['Relative'])
py.iplot([data])

# Plotting with Seaborn - No way to plot pie chart with seaborn


#Creation of pareto Diagram
df.sort_values(by='Relative',ascending=False, inplace=True)
df['cumulative_sum'] = df['Relative'].cumsum()
df['cumulative_perc'] = df['Relative'].cumsum()*100
df

trace1 = go.Bar(
    x=df.index,
    y=df['Sold'],
    name='Sold'
)
trace2 = go.Scatter(
    x=df.index,
    y=df['cumulative_perc'],
    name='Cumulative Sold',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    title='Pareto Diagram Example',
    yaxis=dict(
        title='Sold'
    ),
    yaxis2=dict(
        title='Cumulative Sold',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)

py.iplot(go.Figure(data=data, layout=layout))

# Creation of pareto diagram with seaborn
sns.set_style("white")
fig, ax = plt.subplots()
ax = sns.barplot(x=df.index, y=df['Sold'])
ax2 = ax.twinx()
ax2 = sns.pointplot(x=df.index, y=df['cumulative_perc'], order=["San Francisco", "LA", "New York"], color="Y")
sns.despine(ax=ax, right=True, left=True)
sns.despine(ax=ax2, left=True, right=False)
ax2.spines['right'].set_color('white')
