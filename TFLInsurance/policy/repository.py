import json 

def save_policy(policy):
    with open ("./Data/policy.json", "w") as file :
        json.dump(policy, file)

def get_all_policys():
    with open ("./Data/policy.json", "r") as file :
        policys = json.load(file)
        return policys 

def get_policy_by_id(id):
    with open ("./Data/policy.json", "r") as file :
            policys = json.load(file)
            return policys[id]