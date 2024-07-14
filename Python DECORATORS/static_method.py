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
