import pandas as pd


df=pd.read_csv("policies.csv")
print(df)



highestCoverage=df["Coverage"].apply(lambda p:p>1000000)
print(highestCoverage)

df["discountedPremium"]=df["Premium"].apply(lambda p:p *0.90)
print(df)


newdf=list(df.apply(lambda p:{**p.to_dict(), "discounted_amount":p["Premium"] * 0.90},axis=1))
print(newdf)


df["discountedPremiumStatus"]=df["Premium"].apply(lambda p: "high" if p>25000 else "normal")
print(df)


active_policies = df[
    df["Status"].apply(
        lambda status: status == "Active"
    )
]
print(active_policies)