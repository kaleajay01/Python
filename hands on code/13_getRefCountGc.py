import sys

class Customer:
    pass

customer1=Customer()

customer2=customer1

# get refernce count for the instance
print(sys.getrefcount(customer1))

customer3=Customer()

print(sys.getrefcount(customer3))

# get count for all the instace
print(sys.getrefcount(Customer))
