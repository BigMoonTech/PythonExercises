import math

# Inheritance


class Character:
    

    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
    

class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return f"You found me!"

bob = NPC("Bob", 100, 1)
print(bob.speak())


# Write a Python class named Circle constructed by a radius and 
# two methods which will compute the area and the perimeter of a circle

class Circle:
    

    def __init__(self, radius):
        self.radius = radius


    def __repr__(self):
        return f"radius of {self.radius}. area of {self.area()}. circum of {self.perimeter()}"


    def area(self):
        area = math.pi * (self.radius**2)
        return area


    def perimeter(self):
        circum = 2 * math.pi * self.radius
        return circum


circle = Circle(2.5)
print(circle)