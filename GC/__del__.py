class Customer:
    def __del__(self):
        print("Customer object is destroy")
    
customer = Customer()
