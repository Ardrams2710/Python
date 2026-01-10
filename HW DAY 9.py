class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def _add_(self,other):
        return self.balance + other._balance
class savingsAccount(Account):
    def calculate_interest(self):
        return self.balance*0.05
class currentAccount(Account):
    def calculate_interest(self):
        return self.balance*0.02
savings = savingsAccount("Ravi", 10000)
current = currentAccount("Janvi",15000)
print("savings Account Details")
print("name:",savings.name)
print("balance:",savings.balance)
print("interest:",savings.calculate_interest())
print("current Account Details")
print("name:",current.name)
print("balance:",current.balance)
print("interest:",current.calculate_interest())
total = savings + current
print("Total Balance:", total)



