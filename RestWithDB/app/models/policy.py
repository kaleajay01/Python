from dataclasses import dataclass

@dataclass
class Policy:
    id:int
    policy_number:str
    name:str
    description:str
    maturity:str
    premium:float
    policy_type:str