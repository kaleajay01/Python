# app/repositories/policy_repository.py

from sqlalchemy.orm import Session

from app.models.policy_db import PolicyDB


class PolicyRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(PolicyDB).all()

    # def get_by_id(self, policy_id: int):
    #     return (
    #         self.db.query(PolicyDB)
    #         .filter(PolicyDB.id == policy_id)
    #         .first()
    #     )

    # def create(self, policy_data: dict):
    #     policy = PolicyDB(**policy_data)

    #     self.db.add(policy)
    #     self.db.commit()
    #     self.db.refresh(policy)

    #     return policy

    # def update(self, policy_id: int, policy_data: dict):
    #     policy = self.get_by_id(policy_id)

    #     if policy is None:
    #         return None

    #     for key, value in policy_data.items():
    #         setattr(policy, key, value)

    #     self.db.commit()
    #     self.db.refresh(policy)

    #     return policy

    # def delete(self, policy_id: int):
    #     policy = self.get_by_id(policy_id)

    #     if policy is None:
    #         return None

    #     self.db.delete(policy)
    #     self.db.commit()

    #     return policy   


# from sqlalchemy.orm import Session
# from app.models.policy import Policy
# from app.models.policy_db import PolicyDB

# class PolicyRepository:
    
#     def __init__(self, db:Session):
#         self.db =db
        
#     def get_all(self):
#         return self.db.query(PolicyDB).all()

#     # def __init__(self):
#     #     self._policies = {
#     #         1: Policy(
#     #             id=1,
#     #             name="Jeevan Labh",
#     #             description="Life insurance savings plan",
#     #             maturity="10 years",
#     #             premium=15000.0
#     #         ),
#     #         2: Policy(
#     #             id=2,
#     #             name="Jeevan Arogya",
#     #             description="Health insurance plan",
#     #             maturity="5 years",
#     #             premium=12000.0
#     #         ),
#     #         3: Policy(
#     #             id=3,
#     #             name="Jeevan Suraksha",
#     #             description="Family protection plan",
#     #             maturity="15 years",
#     #             premium=20000.0
#     #         )
#     #     }

#     #     self._next_id = 4

#     def get_all(self):
#         return list(self._policies.values())

#     def get_by_id(self, policy_id: int):
#         return self._policies.get(policy_id)

#     def create(self, policy_data: dict):
#         policy = Policy( id=self._next_id,**policy_data        )
#         self._policies[policy.id] = policy
#         self._next_id += 1

#         return policy

#     def update(self, policy_id: int, policy_data: dict):
#         if policy_id not in self._policies:
#             return None
#         updated = Policy(id=policy_id,**policy_data)
#         self._policies[policy_id] = updated
#         return updated

#     def delete(self, policy_id: int):
#         return self._policies.pop(policy_id, None)