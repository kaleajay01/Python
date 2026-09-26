class Employee:
    def __init__(self,name,salary,contactNumber):
        self.name=name
        self.salary=salary
        self.contactNumber=contactNumber
    
    def showDetails(self):
        print(f"Full Name: {self.name} salary:{self.salary} contact Number: {self.contactNumber}")

    def sendMoney(self, amount):
        self.salary=self.salary-amount
    
e1=Employee("sanika",50000,"8446756339")
e2=Employee("Sumit",78000,"8530086989")
e3=Employee("prachi",50000,"7896325410")

e1.showDetails()
e1.sendMoney(5000)
e1.showDetails()

e2.showDetails()