from abc import ABC, abstractmethod
class user(ABC):
    def __init__(self,name,account_year):
        self.name=name
        self.account_year=account_year
    def account_age(self):
        account_year=2025
        return account_year-self.account_year
    @abstractmethod
    def get_role(self):
        pass
class admin(user):
    def get_role(self):
        return "admin"
    def __str__(self):
        return "The admin user is " + self.name
class guest(user):
    def get_role(self):
        return "guest"
    def __str__(self):
        return "The guest user is " + self.name
admin_user = admin("Abhirami", 2019)
guest_user = guest("Anaswara", 2023)
print(admin_user.get_role())
print(admin_user.account_age())
print(admin_user)
print()
print(guest_user.get_role())
print(guest_user.account_age())
print(guest_user)

