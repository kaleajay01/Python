class Claim:

    def __init__( self, claim_id, policy_id, amount, reason ):
        self.claim_id = claim_id
        self.policy_id = policy_id
        self.amount = amount
        self.reason = reason
        self.status = "Submitted"

    def __str__(self):
        return ( f"Claim ID: {self.claim_id}, " f"Policy ID: {self.policy_id}, "f"Amount: {self.amount}, " f"Reason: {self.reason}, " f"Status: {self.status}" )