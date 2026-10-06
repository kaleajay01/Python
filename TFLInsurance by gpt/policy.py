from enum import Enum
from datetime import date

class PolicyType(Enum):
    HEALTH = "Health"
    LIFE = "Life"
    VEHICLE = "Vehicle"
    
class PolicyStatus(Enum):
    ACTIVE = "Active"
    EXPIRED = "Expired"
    CANCELLED = "Cancelled"

class Policy:

    def __init__(self, id, policy_number, policy_type, customer, coverage_amount, policy_duration_year, start_date, policy_status, premium):
        self.id = id
        self.policy_number = policy_number
        self.policy_type = policy_type
        self.customer = customer
        self.coverage_amount = coverage_amount
        self.policy_duration_year = policy_duration_year
        self.start_date = start_date
        self.policy_status = policy_status
        self.premium = premium

    def display(self):
        print("ID:", self.id)
        print("Policy Number:", self.policy_number)
        print("Policy Type:", self.policy_type)
        print("Customer:", self.customer)
        print("Coverage Amount:", self.coverage_amount)
        print("Policy Duration (Years):", self.policy_duration_year)
        print("Start Date:", self.start_date)
        print("Policy Status:", self.policy_status)
        print("Premium:", self.premium)