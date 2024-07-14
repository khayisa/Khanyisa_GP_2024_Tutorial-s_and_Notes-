class Circle:
    def __init__(self, radius):
        # Initialize the Circle with a private _radius attribute
        self._radius = radius

    @property
    def radius(self):
        """Get the radius of the circle."""
        # The property decorator allows this method to be accessed as an attribute
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the circle. Must be positive"""
        # The setter decorator allows setting the value of the radius with validation
        if value >= 0:
            self._radius = value  # Update the private _radius attribute
        else:
            # Raise an error if the provided value is negative
            raise ValueError("Radius must be positive")

    @property
    def diameter(self):
        """Get the diameter of the circle."""
        # Calculate and return the diameter based on the radius
        return self._radius * 2

# Usage examples

# Create a Circle object with a radius of 5
c = Circle(5)

# Access the radius property (calls the radius getter method)
print(c.radius)  # Output: 5

# Access the diameter property (calls the diameter getter method)
print(c.diameter)  # Output: 10

# Set a new radius value using the radius setter method
c.radius = 10

# Access the updated radius property
print(c.radius)  # Output: 10

# Access the updated diameter property
print(c.diameter)  # Output: 20
