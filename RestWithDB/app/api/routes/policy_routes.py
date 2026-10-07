from fastapi import(APIRouter,Depends,HTTPException,Request,status)
from app.schemas.policy_schema import(PolicyCreate,PolicyUpdate,PolicyResponse)
from app.services.policy_service import PolicyService
from app.models.policy import Policy

router=APIRouter(prefix="/api/policies", tags=["Policies"])

def get_policy_service(request: Request) -> PolicyService:
    return request.app.state.policy_service
    
@router.get("/")
def get_all_policies(service:PolicyService=Depends(get_policy_service)):
    policies=service.get_all_policies()
    
    return {
        "message":"policies reteives successfully",
        "count":len(policies),
        "data":policies
    }

@router.get("/{id}")
def get_policy_by_id(id: int, service: PolicyService=Depends(get_policy_service)):
    policy=service.get_policy_by_id(id)
    
    return{
        "message":"policies reteives successfully",
        "data":policy
        }   

@router.post("/addpolicy")
def create_policy_new(policy: Policy, service: PolicyService=Depends(get_policy_service)):
    id=service.create_new_policy(policy)
    
    return{
        "message":"policy added successfully",
        "new policy id":id
    }
    
@router.put("/{id}")
def update_policy(id: int, policy: Policy, service: PolicyService=Depends(get_policy_service)):
    policy=service.update_policy(id,policy)
    
    return{
        "message":"updated policy",
        "data":policy
    }


@router.delete("/{id}")
def removed_policy(id: int, service: PolicyService=Depends(get_policy_service)):
    policy = service.delete_policy(id)
    
    return{
        "message":"policy deleted successfully"
    }