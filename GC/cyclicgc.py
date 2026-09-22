import gc

class Customer:
    pass

class InsurancePolicy:
    pass

# Create two objects
customer = Customer()
policy = InsurancePolicy()

# Create a circular reference
customer.policy = policy
policy.customer = customer

# Remove the external references
del customer
del policy

# Ask Python to collect unreachable objects
collected = gc.collect()

print("Objects collected:", collected)