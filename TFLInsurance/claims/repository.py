import json 

def save_claim(claim):

    with open("./Data/claims.json", "w") as file:
        json.dump(claim, file, indent=4)



def get_all_claims():
    with open("./Data/claims.json", "r") as file:
        claims = json.load(file)
    return claims
