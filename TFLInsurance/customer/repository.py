import json 

def save_customer(x):
    with open("./Data/customers.json", "r") as file:
        customers = json.load(file)
    customers.append({
        "customer_id": customer.customer_id,
        "name": customer.name,
        "email": customer.email,
        "phone": customer.phone
    })

    with open("./Data/customers.json", "w") as file:
        json.dump(customers, file, indent=4)


def get_all_customers():
    with open ("./Data/customers.json", "r") as file :
        customers = json.load(file)
        return customers 

def get_customer_by_id(id):
    with open ("./Data/customers.json", "r") as file :
            customers = json.load(file)
            return customers[id]
        