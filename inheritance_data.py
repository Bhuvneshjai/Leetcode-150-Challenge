'''
Inheritance: Allows a new class (child class) to inherit attributes and methods from an existing class
(parent class). This promotes code reusability.
'''

class Animal:
    def speak(self):
        return "Animal Speaks"

class Dog(Animal):
    def speak(self):        #Dog inherits from Animal
        return "Woof!"

class Cat(Animal):
    def speak(self):        #Cat inherits from Animal
        return "Meeow!"

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())