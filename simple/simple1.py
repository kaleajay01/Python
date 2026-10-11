import pandas as pd

data = {
    "name":["Ajay","Sanika","Rahul"],
    "Age":[22,21,22],
    "Salary":[500,500,500]
}

df = pd.DataFrame(data)
print(df)