import pandas as pd 

df=pd.read_csv('Data/main_data/air_quality_index.csv')
print(df.shape)
print(df.isna().sum())
df.dropna(inplace=True)
print(df.shape)
print(df.isna().sum())
print(df)
