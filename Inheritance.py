#Inheritance allows a class (the child or derived class) to inherit attributes and methods from another class (the parent or base class).

#Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "some sound"
    
#Derived class
class Dog(Animal):
    """
    Inheritance allows a child class to inherit and override methods and attributes from a parent class.
    """
    def speak(self): #overriding
        return "Bark"
    

if __name__ == "__main__":
    dog = Dog("Buddy")
    print(dog.name) #Inherited attribute
    print(dog.speak()) # Overridden method


