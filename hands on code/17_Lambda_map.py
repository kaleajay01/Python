policies = [
    {"name": "Policy A", "premium": 50000},
    {"name": "Policy B", "premium": 30000},
]

discounted_list=list(
    map(
        lambda p: {
        **p,
        "discounted_amount": p["premium"] *0.95
        },
        policies
        ))


print(discounted_list)


