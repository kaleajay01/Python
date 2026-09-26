policies = [
    {"name": "Policy A", "premium": 50000},
    {"name": "Policy B", "premium": 30000},
]


higestPremium=list(filter(lambda p: p["premium"]>=50000,policies))
print(higestPremium)