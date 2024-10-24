import pandas as pd
from functools import reduce

# Load your CSV files
df1 = pd.read_csv('scoop.csv')
df2 = pd.read_csv('act.csv')
df3 = pd.read_csv('flavia.csv')

dataframes = [df1, df2, df3]

intersection = reduce(lambda left, right: pd.merge(left, right, on='Top Traders'), dataframes)

intersection.to_csv('intersection.csv', index=False)

print("Intersection saved to 'intersection.csv'.")
