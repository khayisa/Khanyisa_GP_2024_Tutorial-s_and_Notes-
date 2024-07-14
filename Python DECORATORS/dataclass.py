class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        # Initialize the Product object with name, price, and optional quantity
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self) -> float:
        # Calculate and return the total cost of the product (price * quantity)
        return self.price * self.quantity

    def __repr__(self):
        # Return a string representation of the Product object for debugging and logging
        return (
            f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"
        )

    def __eq__(self, other):
        # Check if two Product objects are equal by comparing their attributes
        if not isinstance(other, Product):
            return NotImplemented
        
        return (
            self.name == other.name
            and self.price == other.price
            and self.quantity == other.quantity
        )
