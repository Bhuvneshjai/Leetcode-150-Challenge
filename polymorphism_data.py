'''
Polymorphism: Allows methods to do different things based on the object that it is acting upon. Enables the
same methods name to be used for different types.
'''

class Bird:
    def fly(self):
        return "Flies in the sky"

class Penguin(Bird):
    def fly(self):
        return "Cannot Fly"

def make_it_fly(bird):
    print(bird.fly())

sparrow = Bird()
penguin = Penguin()
print(sparrow.fly())
print(penguin.fly())