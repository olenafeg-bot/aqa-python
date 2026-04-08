import math
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2
class Square(Figure):
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width * self.width
    def perimeter(self):
        return self.width * 4

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

rectangle = Rectangle(15, 9)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

square = Square(7)
print("Square area:", square.area())
print("Square perimeter:", square.perimeter())

circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())