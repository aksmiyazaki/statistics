import pandas as pd
import seaborn as sns
from sklearn import preprocessing

df = pd.read_csv("/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/34.csv")

sns.distplot(df['Original dataset'])

#Standardization by hand
df['Original dataset'].mean()
df['Original dataset'].std()
df['Standardized dataset'] = (df['Original dataset'] - df['Original dataset'].mean())/df['Original dataset'].std()

sns.distplot(df['Standardized dataset'])

#Standardization using sklearn
df = pd.read_csv("/home/aksmiyazaki/git/statistics/udemy_statistics_for_ds/34.csv")
scaler = preprocessing.StandardScaler()
scaled_df = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_df, columns=['Standardized dataset'])
sns.distplot(scaled_df['Standardized dataset'])
