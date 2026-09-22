class Policy:

    def __init__( self, policy_id, customer_id, policy_type, sum_insured, premium):
        self.policy_id = policy_id
        self.customer_id = customer_id
        self.policy_type = policy_type
        self.sum_insured = sum_insured
        self.premium = premium

    def __str__(self):
        return (
            f"Policy ID: {self.policy_id}, "
            f"Customer ID: {self.customer_id}, "
            f"Type: {self.policy_type}, "
            f"Sum Insured: {self.sum_insured}, "
            f"Premium: {self.premium}"
        )