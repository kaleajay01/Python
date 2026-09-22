class Customer:

    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return (
            f"Customer ID: {self.customer_id}, "
            f"Name: {self.name}, "
            f"Email: {self.email}, "
            f"Phone: {self.phone}"
        )
        