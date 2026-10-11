import pandas as pd

data = {
    "PolicyID": ["POL1001","POL1002","POL1003","POL1004","POL1005" ],
    "Customer": ["Ravi","Amit","Sneha","Priya","Rahul"],
    "Product": ["Life Protection", "Child Future", "Life Protection", "Retirement","Child Future"],
    "Premium": [25000,40000,15000,60000,30000],
    "Coverage": [1000000,2000000,500000,3000000,1500000],
    "Status": ["Active", "Active", "Inactive", "Active", "Active"]
}

df = pd.DataFrame(data)
# print(df)

high_coverage = df[
    df["Coverage"].apply(
        lambda coverage: coverage > 500000
    )
]
print("High coverage policy",high_coverage)

# add new column
# in existing dataframe
print("discounted premium:")
df["DiscountedPremium"] = df["Premium"].apply(
    lambda premium: premium * 0.90
)
print(df)

# create new dataframe
print("new data")
new_data = {
    **data,
    "Discount": [0.10, 0.15, 0.00, 0.20, 0.10]
}
print("old",data)
print("new",new_data)


# descending sorted by premium
print("sorted by premium DSC:")
sorted_df = df.sort_values(
    by="Premium",
    ascending=False
)
print(sorted_df)

# ascending
print("sorted by premium ASC:")
sorted_df = df.sort_values(
    by="Premium",
)
print(sorted_df)