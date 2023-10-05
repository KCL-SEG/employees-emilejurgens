"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, pay, hours, commission, contracts=0):
        self.name = name
        self.contract = contract
        self.pay = pay
        self.hours = hours
        self.commission = commission
        self.contracts = contracts

    def get_pay(self):
        wages = 0
        if self.contract == "salary":
            wages = self.pay
        elif self.contract == "wage":
            wages =  self.pay * self.hours

        if self.commission > 0:
            if self.contracts > 0:
                wages += self.commission * self.contracts
            else:
                wages += self.commission
        
        return wages
    

    def __str__(self):
        string = ""
        if self.contract == "salary" and self.commission == 0:
            string = f"{self.name} works on a monthly salary of {self.pay}.  Their total pay is {self.get_pay()}."
        elif self.contract == "wage" and self.commission == 0:
            string = f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour.  Their total pay is {self.get_pay()}."
        elif self.contract == "salary" and self.commission != 0 and self.contracts == 0:
            string = f"{self.name} works on a monthly salary of {self.pay} and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}."
        elif self.contract == "wage" and self.commission != 0 and self.contracts == 0:
            string = f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}."
        elif self.contract == "salary" and self.commission != 0 and self.contracts != 0:
            string = f"{self.name} works on a monthly salary of {self.pay} and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."
        elif self.contract == "wage" and self.commission != 0 and self.contracts != 0:
            string = f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "salary", 4000, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "wage", 25, 100, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "salary", 3000, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "wage", 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "salary", 2000, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "wage", 30, 120, 600)
