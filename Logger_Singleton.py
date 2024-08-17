class Logger:
    _instance = None  # Class-level attribute to hold the single instance of the Logger

    def __new__(cls, *args, **kwargs):
        """
        In __new__:

        cls is used to refer to the class that is being instantiated.
        *args and **kwargs allow __new__ to accept any number of positional and keyword arguments 
        that might be passed during the creation of an object.
        In __init__:

        While __new__ creates the object, __init__ initializes it. 
        The same pattern can be used in __init__ to ensure that any arguments passed to the constructor are handled properly.
        
        """
        # __new__ is called before __init__, and is responsible for creating a new instance of the class
        if not cls._instance:
            # If no instance exists, create a new one using the parent class's __new__ method
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        # Return the single instance (existing or newly created)
        return cls._instance

    def log(self, message):
        # A simple method to log a message (in this case, print to console)
        print(f"Log: {message}")


class Example:
    def __new__(cls, *args, **kwargs):
        # __new__ is responsible for creating the new instance
        print("In __new__")
        print(f"cls: {cls}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        instance = super(Example, cls).__new__(cls)
        return instance

    def __init__(self, *args, **kwargs):
        # __init__ initializes the instance
        print("In __init__")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        self.data = args if args else kwargs


if __name__ == "__main__":
    # Usage
    logger1 = Logger()  # Creates the first instance of Logger
    logger2 = Logger()  # Returns the existing instance, no new instance is created

    print(logger1 == logger2)  # Output: True, proving both logger1 and logger2 are the same instance

    logger1.log("This is a singleton logger.")  # Logs a message using the singleton instance

    # Creating an instance of Example
    ex = Example(10, 20, key="value")