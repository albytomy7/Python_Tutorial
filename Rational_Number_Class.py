import math

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    # Reduce fraction using GCD (Euclid's Algorithm)
    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    # String representation
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # Accessors
    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    # Addition
    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)

    # Subtraction
    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)

    # Multiplication
    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Rational(num, den)

    # Equal comparison
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    # Less than
    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    # Greater than
    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator


# Example usage
r1 = Rational(1, 2)
r2 = Rational(3, 4)

print("r1:", r1)
print("r2:", r2)

print("Addition:", r1 + r2)
print("Subtraction:", r1 - r2)
print("Multiplication:", r1 * r2)

print("r1 == r2:", r1 == r2)
print("r1 < r2:", r1 < r2)
print("r1 > r2:", r1 > r2)