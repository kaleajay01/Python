policies = [
    {"name": "Policy A", "premium": 50000},
    {"name": "Policy B", "premium": 30000},
    {"name": "Policy z", "premium": 30000},
    {"name": "Policy g", "premium": 30000},
    {"name": "Policy m", "premium": 30000},

]


sortedlistdesc=list(sorted(policies,key=lambda p: p["name"], reverse=True))

sortedlistasc=list(sorted(policies,key=lambda p: p["name"]))

print("decending:" ,sortedlistdesc)
print("Asecnding:",sortedlistasc)