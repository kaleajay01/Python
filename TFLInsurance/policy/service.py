from policy.Policy import Policy
from policy.repository import (save_policy , get_all_policys)


policies = get_all_policys()


def calculate_premium(sum_insured):
    return sum_insured * 0.05


def create_policy():

    policy_id = len(policies) + 1

    customer_id = int(input("Enter customer ID: "))
    policy_type = input("Enter policy type: ")
    sum_insured = float(input("Enter sum insured: "))

    premium = calculate_premium(sum_insured)

    policy = Policy( policy_id, customer_id, policy_type, sum_insured, premium )

    save_policy(policy)

    print("Policy created successfully.")
    print(policy)


def get_policy():

    policy_id = int(input("Enter policy ID: "))

    for policy in policies:

        if policy.policy_id == policy_id:
            print(policy)
            return policy

    print("Policy not found.")
    return None