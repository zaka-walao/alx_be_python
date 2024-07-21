import math

class Shape:
    def area(self):
        """
        Base method to be overridden in derived classes.
        Raises an error if called directly without overriding.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle using the formula π * r^2.
        """
        return math.pi * self.radius ** 2

# These classes utilize polymorphism by allowing them to use a common interface (area()) with different implementations.
