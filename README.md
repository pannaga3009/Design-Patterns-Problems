# Design-Patterns-Problems


## 1. Interface:

An interface is a contract that specifies a set of methods that a class must implement, without dictating how these methods should be implemented. In languages like Python, interfaces are typically represented using abstract base classes (ABCs) with abstract methods.

Purpose: To define a common protocol for a group of classes. Any class that implements an interface agrees to provide implementations for all the methods declared in the interface.

Use Case: When you want to ensure that different classes have a common set of methods, but you don't care how these methods are implemented.

Example: Suppose you have different types of media players (e.g., audio player, video player). You can define an interface MediaPlayer with methods like play(), pause(), and stop(). Any media player class would then be required to implement these methods.


## 2. Abstract Class:

An abstract class is a class that cannot be instantiated on its own and is meant to be a blueprint for other classes. It can contain both concrete methods (methods with implementations) and abstract methods (methods without implementations).

Purpose: To provide a base class with some common functionality that can be shared among subclasses, while also enforcing certain methods to be implemented by the subclasses.

Use Case: When you want to provide shared code among related classes, but also want to ensure that certain methods are implemented in all subclasses.

Example: Suppose you have a base class Shape with a method area() that must be implemented by all shapes (like Circle, Square). You can define Shape as an abstract class with a concrete method describe() and an abstract method area().