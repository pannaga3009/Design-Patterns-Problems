# Python does not have a built-in interface keyword like some other languages (e.g., Java). 
# Instead, you can define an interface using abstract base classes (ABCs) with the abc module.
# An abstract base class can have abstract methods that must be implemented by any subclass.

#Interfaces are like contracts ensuring that certain methods are implemented by any class that adheres to them, 
# without dictating how they should be implemented.
from abc import ABC, abstractmethod

#Abstract base case as Interface
#Abstract Base Classes (ABCs) with the abc module are used to define interfaces and abstract classes in Python.
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Use an Interface (Abstract Base Class with only abstract methods):
# When you need to define a common protocol for multiple classes
#  that don't share any implementation details.
# When you want to ensure that all implementing classes provide specific methods,
#  but you don't want to provide any shared code.
# Concrete Class Implementing the Interface   
class Dog(Animal):
    def speak(self):
        pass
    
# Concrete Class Implementing the Interface
class Dog(Animal):
    def speak(self):
        return "Bark"
    

if __name__ == "__main__":
    dog = Dog()
    print(dog.speak())
    