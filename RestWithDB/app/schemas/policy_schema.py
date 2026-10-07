from pydantic import BaseModel, Field


#limitations 
class PolicyCreate(BaseModel):
    policy_number:str
    name: str=Field(min_length=2, max_length=100)
    description:str=Field(min_length=2, max_length=100)
    maturity:str
    premium:float=Field(gt=0)
    policy_type:str


class PolicyUpdate(PolicyCreate):
    pass

class PolicyResponse(PolicyCreate):
    id:int