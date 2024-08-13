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

# Books.py follows Strategy Pattern

## Explanation:
**Strategy Design Pattern**:

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. The algorithm can vary independently from clients that use it.
Why This Code Uses the Strategy Pattern:

- Encapsulation of Algorithms: The BookFilter abstract class defines an interface for filtering strategies. The specific filter implementations (TitleFilter and BookSizeFilter) encapsulate different filtering strategies (by title and by size).
- Interchangeable Strategies: The filtering strategies (TitleFilter and BookSizeFilter) are interchangeable. You can easily add, remove, or combine different filters without modifying the client code (i.e., the code that uses the filters).
- Flexibility: This approach allows for flexibility in defining how books are filtered. The filter_books function can apply any combination of filtering strategies provided, allowing different filtering behaviors depending on the user's needs.

## Key Characteristics of the Strategy Pattern in This Code:
- Context: The filter_books function acts as the context that uses the filtering strategies. It doesn’t know the specifics of each filter but relies on the BookFilter interface to apply the filters.

- Strategy Interface: The BookFilter abstract class serves as the strategy interface, defining the method apply that all concrete strategies must implement.

- Concrete Strategies: The TitleFilter and BookSizeFilter classes are concrete strategies that implement the BookFilter interface, each providing its own filtering logic.

**Benefits of Using the Strategy Pattern**:
- Open/Closed Principle: You can add new filter types (strategies) without altering existing code, adhering to the open/closed principle.
- Reusability: The filter strategies are reusable across different contexts where book filtering might be needed.
- Maintainability: The filtering logic is decoupled from the main application logic, making the code easier to maintain and extend.