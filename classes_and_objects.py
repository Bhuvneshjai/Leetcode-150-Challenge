'''
Classes & Objects
'''

class Dog:
    def __init__(self, name, age):
        self.name = name    #Attribute
        self.age = age      #Attribute

    def bark(self):         #Method
        return "Woof!"

# Creating Object of the Dog class
my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.age)
print(my_dog.bark())