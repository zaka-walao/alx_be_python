class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not require access to any class or instance properties.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Uses a class attribute to print the type of calculation.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b