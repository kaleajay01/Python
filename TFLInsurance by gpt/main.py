import customer
try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Age must contain numbers only.")
    
customer1 = customer.Customer(1, "Ajay", 22, "9876543210", "ajay@gmail.com", "Pune")

# print(customer1.check_eligible())
# print(customer1.display())