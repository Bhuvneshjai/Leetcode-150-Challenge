'''
Encapsulation: Encapsulation is one of the core concepts of Object-Oriented Programming (OOP).
It means binding data (variables) and methods (functions) together into a single unit (a class),
and restricting direct access to some of the object's components.

🎯 Purpose:
Hide internal details (data protection)
Control access to variables
Prevent unintended modification of data

🧱 Access Modifiers in Python:
Python uses convention, not strict rules, for access control:
Modifier	    Syntax	        Access Level
Public	        self.name	    Accessible from anywhere
Protected	    self._name	    Accessible inside class & subclasses
Private	        self.__name	    Accessible only within the class

🔒 Why Use Private and Protected?
To protect internal object state
To prevent misuse or direct tampering of sensitive data
To encourage the use of getter/setter methods for controlled access

✅ What are Getter and Setter?
Getter method: used to get the value of a private variable.
Setter method: used to set or update the value of a private variable in a controlled way.
'''

class BankAccount:
    def __init__(self):
        self.__balance = 0

    # Getter Method
    def get_balance(self):
        return self.__balance

    # Setter Method
    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid Amount!")

# Create Object
acc = BankAccount()

# Set Balance using setter
acc.set_balance(1000)

# Get Balance using getter
print(f"Current Balance: {acc.get_balance()}")