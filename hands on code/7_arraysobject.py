team={
    "teamName":"CodeXplores",
    "founded":2025,
    "members":["Sanika","Prachi","sumit","nirjala","sahil","samruddhi"],
    "location":(190.25,79.004) #tuple (latitude, longitude)
}

print(team)
print(team["teamName"])
print(team["members"][2])
print(team["location"][0])
print(team["founded"])

hackthon={
    "name":"mahaHackthon",
    "duration":"5days",
    "coordinator":"Ravi Tambade",
    "isOnline":True,
    "teams":[
        {
            "teamName":"CodeXplores",
            "founded":2025,
            "members":["Sanika","Prachi","sumit","nirjala","sahil","samruddhi"],
            "location":(190.25,79.004) #tuple (latitude, longitude)
        },
        {
            "teamName":"codingNinja",
            "founded":2026,
            "members":["nikita","rutuja","yash","ajay","rahul",],
            "location":(190.25,79.004) #tuple (latitude, longitude)
        }
   
    ],
    "scheduleOn":(2024,9,21)
}

print(hackthon["teams"][0]["members"])


indians = {
    "state": [
        {
            "name": "Maharashtra",
            "districts": [
                {
                    "name": "Pune",
                    "city": "Pune",
                    "people": [
                        {"name": "Abhay", "age": 27},
                        {"name": "Anish", "age": 28},
                        {"name": "Ujwal", "age": 22}
                    ]
                },
                {
                    "name": "Raigad",
                    "city": "Mumbai",
                    "people": [
                        {"name": "Neeta", "age": 27},
                        {"name": "Sameer", "age": 28},
                        {"name": "Manish", "age": 22}
                    ]
                }
            ]
        },
        {
            "name": "Punjab",
            "districts": [
                {
                    "name": "Amritsar",
                    "city": "Amritsar",
                    "people": [
                        {"name": "Simran", "age": 25},
                        {"name": "Gurpreet", "age": 30},
                        {"name": "Harpreet", "age": 26}
                    ]
                },
                {
                    "name": "Ludhiana",
                    "city": "Ludhiana",
                    "people": [
                        {"name": "Raj", "age": 29},
                        {"name": "Kiran", "age": 27},
                        {"name": "Deep", "age": 24}
                    ]
                }
            ]
        }
    ]
}

print(indians["state"][0]["name"])