#An abstract class in Python is a class that cannot be instantiated on its own and
#  typically contains one or more abstract methods. 
# Abstract methods are defined in the abstract class and must be implemented by any subclass.

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        """
        Abstract classes allow you to define some common behavior while still requiring subclasses 
        to provide specific implementations. 
        They offer more flexibility than interfaces because they can contain
          both abstract and concrete methods.
        """
        self.color = color
    
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return f"A {self.color} shape"
    
# Concrete Class Implementing the Abstract Class
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)
    
if __name__ == "__main__":
    circle = Circle("red", 2)
    print(circle.describe())
    print(circle.area())