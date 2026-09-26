import pandas as pd
data = {
    "PolicyID": ["POL1001","POL1002","POL1003","POL1004","POL1005" ],
    "Customer": ["Ravi","Amit","Sneha","Priya","Rahul"],
    "Product": ["Life Protection", "Child Future", "Life Protection", "Retirement","Child Future"],
    "Premium": [25000,40000,15000,60000,30000],
    "Coverage": [1000000,2000000,500000,3000000,1500000],
    "Status": ["Active", "Active", "Inactive", "Active", "Active"]
}

df=pd.DataFrame(data)
print(df)