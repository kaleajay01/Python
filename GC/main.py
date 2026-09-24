import sys
import gc
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age     
class InsurancePolicy:
    pass

customer1 = Customer("Ajay",22)
customer2 = customer1
# # policy = InsurancePolicy()

customer3=Customer("Sanika",21)
# del
print(sys.getrefcount(Customer))
print(sys.getrefcount(customer1))


print(gc.get_threshold())
print(gc.get_count())

import sys

print(sys.version)