# Python Decorators 
#### what is a decorator ?
A decorator in Python is a design pattern that allows you to modify the behavior of a function or method. It is essentially a function that takes another function as an argument and extends or alters its behavior without explicitly modifying it. Decorators are often used for logging, access control, memoization, and other cross-cutting concerns.

## Writing a custom decorator 

#### Importing Required Module
```python
import time
```
- This line imports the `time` module, which provides various time-related functions.

#### Defining the Decorator Function
```python
def timer(func): 
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__!r} took: {end_time - start_time:.4f} sec")
        return result
    return wrapper
```
1. **timer(func)**: This is the decorator function. It takes one argument, `func`, which is the function to be decorated.
2. **wrapper(*args, **kwargs)**: This inner function, `wrapper`, is defined to accept any number of positional (`*args`) and keyword arguments (`**kwargs`). This makes it flexible enough to wrap any function regardless of its signature.
3. **start_time = time.time()**: This line records the current time (in seconds since the epoch) at the start of the function call.
4. **result = func(*args, **kwargs)**: This line calls the original function (`func`) with its arguments and stores the result.
5. **end_time = time.time()**: This line records the current time after the function has executed.
6. **print(...)**: This prints the name of the function and the time it took to execute. `func.__name__` gives the name of the function, and `!r` is used to get a string representation of it. The time taken is calculated as the difference between `end_time` and `start_time`.
7. **return result**: This returns the result of the original function call.
8. **return wrapper**: This returns the `wrapper` function, effectively replacing the original function with the wrapped version.

#### Defining a Function to Be Decorated
```python
def example_function(n):
    return f"The sum is {sum(range(n))}"
```
- This is a simple function that takes an integer `n`, calculates the sum of numbers from `0` to `n-1`, and returns a formatted string with the result.

#### Applying the Decorator
```python
example_function = timer(example_function)
```
- Here, we apply the `timer` decorator to `example_function`. This is equivalent to using the `@timer` syntax above the function definition. The `example_function` is replaced by the `wrapper` function returned by `timer`.

#### Calling the Decorated Function
```python
print(example_function(1000000))
```
- This calls the decorated version of `example_function` with `1000000` as the argument. The steps inside the `wrapper` function are executed:
  1. The start time is recorded.
  2. The original `example_function` is called, which calculates the sum of the numbers from `0` to `999,999`.
  3. The end time is recorded.
  4. The execution time is printed.
  5. The result of the original function is returned and printed.

## Property decorator @property

```python
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
```
 
## Static-method decorator @staticmethod

```python 
class Math:
    @staticmethod
    def add(x, y):
        # This static method takes two arguments, x and y, and returns their sum.
        return x + y

    @staticmethod
    def multiply(x, y):
        # This static method takes two arguments, x and y, and returns their product.
        return x * y

# Usage examples

# Call the static method add from the Math class with arguments 5 and 7
print(Math.add(5, 7))  # Output: 12

# Call the static method multiply from the Math class with arguments 3 and 4
print(Math.multiply(3, 4))  # Output: 12


```
## Class-method decorator @classmethod
```python 
class Person:
    # Class attribute shared by all instances of the class
    species = "Homo sapiens"

    @classmethod
    def get_species(cls):
        # This class method takes the class itself as the first argument (cls)
        # and returns the value of the class attribute 'species'
        return cls.species

# Usage example

# Call the class method get_species from the Person class and print the result
print(Person.get_species())  # Output: Homo sapiens

```
## Functools.cache

```python
import functools

@functools.cache
def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n < 2:
        return n
    
    # Recursive case: compute Fibonacci number recursively
    return fibonacci(n - 1) + fibonacci(n - 2)

# Calculate and print the 10th Fibonacci number
print(fibonacci(10))

```
## Data class 
```python 
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

```