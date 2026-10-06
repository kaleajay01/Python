class Customer:
    def __init__(self, id, name, age, mobile_number, email, address):
        self.id = id
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.email = email
        self.address = address

    def display(self):
        print("Id:", self.id)
        print("Customer:", self.name)
        print("Age:", self.age)
        print("Mobile_number:", self.mobile_number)
        print("Email:", self.email)
        print("Address:", self.address)
        
    def check_eligible(self):
        if self.age >= 18:
            print("Customer is eligible to purchase the insurance policy")
        else:
            print("Not eligible")