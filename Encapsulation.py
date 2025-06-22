'''
Encapsulation: Bundling of data (attributes) and methods (Function) that operate on the data within a single unit
(Class). Restricts direct access to some of the object's components, which can prevent the accidental modification
of data.
'''

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance        #Private Attribute

    def deposit(self, amount):
        if amount>0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(500)
account.withdraw(200)
print(account.get_balance())