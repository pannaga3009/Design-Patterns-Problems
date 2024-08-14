# Strategy interface
class DiscountStrategy:
    
    def apply_discount(self, price):
        # Method to be implemented by all concrete strategies.
        # This method will apply a discount to the given price.
        pass  # Placeholder method, to be overridden by subclasses.

# Concrete strategies
class RegularDiscount(DiscountStrategy):
    def apply_discount(self, price):
        # Apply a regular discount of 10% to the price.
        return price * 0.90  # 10% off

class ChristmasDiscount(DiscountStrategy):
    def apply_discount(self, price):
        # Apply a Christmas discount of 20% to the price.
        return price * 0.80  # 20% off

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        # Apply no discount, return the price as is.
        return price  # No discount

# Context
class Order:
    def __init__(self, price, discount_strategy: DiscountStrategy):
        # Initialize the order with a price and a discount strategy.
        self.price = price  # Set the price of the order.
        self.discount_strategy = discount_strategy  # Set the discount strategy (an instance of a class implementing DiscountStrategy).

    def get_final_price(self):
        # Calculate the final price after applying the discount strategy.
        return self.discount_strategy.apply_discount(self.price)
        # Returns the final price after applying the discount.

if __name__ == "__main__":



    # Usage
    order = Order(100, RegularDiscount())
    # Create an order with a price of 100 and apply a regular discount.
    print(order.get_final_price())  # Output: 90.0
    # Prints the final price after applying a 10% discount.

    order = Order(100, ChristmasDiscount())
    # Create an order with a price of 100 and apply a Christmas discount.
    print(order.get_final_price())  # Output: 80.0
    # Prints the final price after applying a 20% discount.

    order = Order(100, NoDiscount())
    # Create an order with a price of 100 and apply no discount.
    print(order.get_final_price())  # Output: 100.0
    # Prints the final price without any discount applied.
