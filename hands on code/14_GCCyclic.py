import gc
import sys


class Policy:
    pass

class Customer:
    pass


policy=Policy()
customer=Customer()

policy.customer=customer
customer.policy=policy


print(sys.getrefcount(customer))
print(sys.getrefcount(policy))

del customer
del policy

print(gc.collect())
