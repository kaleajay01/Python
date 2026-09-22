from customer.customer import Customer
from customer.repository import(save_customer , get_all_customers)

customers = get_all_customers()

def create_customer():
    # customer_id = len(customers) + 1
    customer_id=int(input("Enter customer id: "))
    name = input("Enter customer name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    customer = Customer(customer_id, name, email, phone )
    print("Object is created..!")
    save_customer(customer)

    print("Customer created successfully.")
    print(customer)

def get_customer():
    customer_id = int(input("Enter customer ID: "))

    for customer in customers:
    
        if customer["customer_id"] == customer_id:
            print(customer)
            return customer

    print("Customer not found.")
    return None


def update_customer():
    customer_id = int(input("Enter customer ID: "))

    for customer in customers:

        if customer["customer_id"] == customer_id:

            customer["name"] = input("Enter new name: ")
            customer["email"] = input("Enter new email: ")
            customer["phone"] = input("Enter new phone: ")

            print("Customer updated successfully.")
            print(customer)

            return

    print("Customer not found.")