class DivisionByZeroError(Exception):
    def __init__(self, message="Cannot divide by zero"):
        self.message = message
        super().__init__(self.message)

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mul(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return a / b



x = 10
y = 0  # Setting y to 0 to demonstrate division by zero

print(Calculator.add(x, y))

try:
    print(Calculator.div(x, y))
except DivisionByZeroError as e:
    print(e)

 