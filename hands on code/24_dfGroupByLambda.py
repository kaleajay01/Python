import pandas as pd

df=pd.read_csv("policies.csv")
print(df)

productGroupAvg=df.groupby("Product")["Premium"].apply(lambda p: p.mean())
print(productGroupAvg)
