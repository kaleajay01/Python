import pandas as pd


df=pd.read_csv("policies.csv")
print(df)


print("first 5 recoed:",df.head())
print("last 5 recoed:",df.tail())
print("datatype:",df.dtypes)
print("datatype:",df.shape)