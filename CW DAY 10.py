from abc import ABC, abstractmethod 
class user(ABC):
    def __init__(self,name,joining_year):
        self.name=name
        self.joining_year=joining_year
    def calculate(self):
        current_year=2025
        return current_year-self.joining_year
    @abstractmethod
    def get_role(self):
        pass
    def display(self):
        print("name : ",self.name,"\nrole : ",self.get_role(),"\nnumber of years : ",self.calculate())
class customer(user):
    def get_role(self):
        return "customer"
class vendor(user):
    def get_role(self):
        return "vendor"
Customer=customer("Anjana",2020)
Vendor=vendor("Arunima",2021)
Customer.display()
Vendor.display()