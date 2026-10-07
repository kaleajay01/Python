from dataclasses import asdict

from app.repositories.policy_repository import PolicyRepository
from app.models.policy import Policy


class PolicyService:

    def __init__(self, repository: PolicyRepository):
        self.repository = repository

    def get_all_policies(self):
        policies = self.repository.get_all()
        return [asdict(policy) for policy in policies]
    
    def get_policy_by_id(self, id):
        policy = self.repository.get_by_id(id)
        return asdict(policy)
    
    def create_new_policy(self, policy: Policy):
        id = self.repository.add_policy(policy)
        return id
    
    def delete_policy(self, id):
        deleted = self.repository.remove_policy(id)
        return deleted
    
    def update_policy(self, id:int, policy: Policy):
        updatepolicy = self.repository.update_policy(id, policy)
        
        return asdict(updatepolicy)