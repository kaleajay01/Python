import pandas as pd

df=pd.read_csv("policies.csv")
print(df)

sorted_df=df.sort_values(by="Customer",ascending=True)
print(f"\nsorted dataframe by only premium:\n",sorted_df)

sortedcolumn_df=df["Premium"].sort_values(ascending=False)
print(f"\nsorted only premium column in df:\n",sortedcolumn_df)

sortedlambda_df=df.sort_values(by="Customer",key=lambda p:p.str.lower())
print(f"\nsorted only premium column in df:\n",sortedlambda_df)

sortedlambda_df=df.sort_values(by="Customer",key=lambda p:p.str.upper())
print(f"\n df:\n",sortedlambda_df["Customer"].str.upper())

sortedCondition_df = df[df["Premium"] > 25000].sort_values(by="Premium")
print(f"\nsorted dataframe by only premium >25000 :\n",sortedCondition_df)