import pandas as pd
from functools import reduce

# Load your CSV files
df1 = pd.read_csv('scoop.csv')
df2 = pd.read_csv('act.csv')
df3 = pd.read_csv('flavia.csv')
df4 = pd.read_csv('gnon.csv')
df5 = pd.read_csv('tateterm.csv')
df6 = pd.read_csv('fartcoin.csv')
df7 = pd.read_csv('tateai.csv')
df8 = pd.read_csv('egregor.csv')
df9 = pd.read_csv('ant.csv')
df10 = pd.read_csv('gematro.csv')

dataframes = [df4, df9, df10]

intersection = reduce(lambda left, right: pd.merge(left, right, on='Top Traders'), dataframes)

intersection.to_csv('intersection.csv', index=False)

print("Intersection saved to 'intersection.csv'.")
