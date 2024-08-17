# Design-Patterns-Problems

## What Are Design Patterns?
Design patterns are reusable solutions to common problems that occur in software design. They represent best practices used by experienced object-oriented software developers. Design patterns are like templates that can be applied to real-world programming scenarios, helping to solve recurring design challenges in a systematic way.

Why Are They Used?
Design patterns are used to:

- Promote Reusability: By using patterns, you can reuse proven solutions across different projects, reducing the need to solve the same problem multiple times.
- Improve Code Readability and Maintainability: Patterns provide a standard way of structuring code, which makes it easier to understand, maintain, and extend.
- Facilitate Communication: Patterns provide a common language for developers to discuss design solutions, improving communication and collaboration.
- Encourage Best Practices: Patterns are based on best practices, helping to avoid common pitfalls and leading to more robust software designs.
  
## Notes
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

# Strategy Pattern

## Books.py follows Strategy Pattern
### Explanation:
**Strategy Design Pattern**:

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. The algorithm can vary independently from clients that use it.

The Strategy Pattern is a design pattern that allows you to define a family of algorithms, put each of them in a separate class, and make their objects interchangeable. In simpler terms, it's like having multiple ways to do something, and you can choose which way to use without changing the code that uses it.

**How It Works**:
- Define a Strategy Interface: Create an interface (or abstract class) that all strategies (different ways of doing something) will follow. This interface defines a method that all the strategies will implement in their own way.

- Create Concrete Strategies: Implement the strategy interface in different classes, each with its own version of the method. These classes represent different strategies (different ways of doing something).

- Context Class: This class uses a strategy. It doesn't know how the strategy works internally; it just uses the method from the strategy interface. The context class can be configured with any concrete strategy.

Why This Code Uses the Strategy Pattern:

- Encapsulation of Algorithms: The BookFilter abstract class defines an interface for filtering strategies. The specific filter implementations (TitleFilter and BookSizeFilter) encapsulate different filtering strategies (by title and by size).
- Interchangeable Strategies: The filtering strategies (TitleFilter and BookSizeFilter) are interchangeable. You can easily add, remove, or combine different filters without modifying the client code (i.e., the code that uses the filters).
- Flexibility: This approach allows for flexibility in defining how books are filtered. The filter_books function can apply any combination of filtering strategies provided, allowing different filtering behaviors depending on the user's needs.

## Key Characteristics of the Strategy Pattern in This Code:
- Context: The filter_books function acts as the context that uses the filtering strategies. It doesn’t know the specifics of each filter but relies on the BookFilter interface to apply the filters.

- Strategy Interface: The BookFilter abstract class serves as the strategy interface, defining the method apply that all concrete strategies must implement.

- Concrete Strategies: The TitleFilter and BookSizeFilter classes are concrete strategies that implement the BookFilter interface, each providing its own filtering logic.

## Discount_strategy.py uses Strategy Pattern:

- Strategy Interface (DiscountStrategy): Defines the common interface that all discount strategies must implement.
- Concrete Strategies (RegularDiscount, ChristmasDiscount, NoDiscount): These are the different algorithms or strategies, each in its own class.
- Context (Order): Uses a strategy object to apply the discount. The Order class doesn’t care which discount strategy is being used; it just knows how to interact with the strategy.

**Benefits of Using the Strategy Pattern**:
- Open/Closed Principle: You can add new filter types (strategies) without altering existing code, adhering to the open/closed principle.
- Reusability: The filter strategies are reusable across different contexts where book filtering might be needed.
- Maintainability: The filtering logic is decoupled from the main application logic, making the code easier to maintain and extend.

# Singleton Pattern
The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.

## Problem: 
Design a logging system where there should be only one instance of the logger, regardless of how many times it is accessed throughout the application.

## Explanation: 
You need to ensure that there is only one instance of a class, and provide a global point of access to that instance.

## In Logger_Singleton.py:

The __new__ method ensures that only one instance of the Logger class is created.
When Logger() is called, the class checks if an instance already exists. If not, it creates one; otherwise, it returns the existing instance.

# Factory Pattern: 

Provides an interface for creating objects in a super class but allows subclasses to alter the type of objects that will be created. It decouples the client code from the specific classes it needs to instantiate.

The Factory Pattern is a creational design pattern that provides an interface for creating objects, but allows subclasses to alter the type of objects that will be created. In simpler terms, it helps you create objects without specifying the exact class of the object that will be created. 

## Explanation of Document_Factory.py
Document is an abstract base class (ABC) with an abstract method create.

WordDocument, PDFDocument, and ExcelDocument are concrete implementations of the Document class.

DocumentFactory is a factory class with a static method get_document that returns an instance of the requested document type.
The DocumentFactory class contains a static method get_document that returns the appropriate document type based on the input, allowing the client code to remain decoupled from the specific implementations.
This allows the client code to create objects without needing to know the specific class of object being created.