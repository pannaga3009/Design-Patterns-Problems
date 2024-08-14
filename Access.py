class MyClass:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"

    def public_method(self):
        return "Public method"

    def _protected_method(self):
        return "Protected method"

    def __private_method(self):
        return "Private method"


if __name__ == "__main__":

    obj = MyClass()

    # Accessing public members
    print(obj.public_var)  # Output: Public
    print(obj.public_method())  # Output: Public method

    # Accessing protected members (conventionally discouraged)
    print(obj._protected_var)  # Output: Protected
    print(obj._protected_method())  # Output: Protected method

    # Accessing private members (name mangling)
    # print(obj.__private_var)  # Raises AttributeError
    print(obj._MyClass__private_var)  # Output: Private
    print(obj._MyClass__private_method())  # Output: Private method
