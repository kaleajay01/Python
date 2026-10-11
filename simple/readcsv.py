import pandas as pd

df = pd.read_csv("policies.csv")

print(df.head())


high_coverage = df["Coverage"].apply(
        lambda coverage: coverage > 1000000
    )
print("high_coverage:", high_coverage)



df["PremiumCategory"] = df["Premium"].apply(
    lambda premium: "High"
    if premium >= 50000
    else "Normal"
)
print(f"high and normal:\n",df)


print("groupby mean:")
avg_premium = (
    df.groupby("Product")["Premium"]
      .apply(lambda x: x.mean())
)
print(avg_premium)


avg_coverage = (
    df.groupby("Product")["Coverage"]
      .apply(lambda x: x.mean())
)

print("\nAvg coverage:",avg_coverage)



active_policies = df[
    df["Status"].apply(
        lambda status: status == "Active"
    )
]
print("\nAction Policues:\n",active_policies)


active_policies = df.apply(lambda p: p["Status"] == "Active" and p["Coverage"] > 2000000,axis=1)
print("\nAction Policues:\n",active_policies)