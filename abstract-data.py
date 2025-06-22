'''
Abstract: Hiding the complex implementation details and showing only the essential features of the object.
In python, abstraction can be achieved using abstract classes and interfaces.
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(10,5), Circle(5)]
for shape in shapes:
    print(shape.area())