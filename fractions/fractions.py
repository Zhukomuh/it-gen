"""class for create fractions and work with them"""
import math


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise TypeError('Numerator must be int')
        if not isinstance(denominator, int):
            raise TypeError('Denominator must be int')
        if not denominator:
            raise ZeroDivisionError('Denominator must be > 0')
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        sign = 1 if self.numerator * self.denominator > 0 else -1
        if other.denominator < 0:
            other.numerator *= -1
        if abs(self.denominator) == abs(other.denominator):
            denominator = abs(self.denominator)
            numerator = other.numerator + abs(self.numerator)
            return Fraction(sign * numerator, denominator)
        nok = (abs(self.denominator) * abs(other.denominator)) // \
              math.gcd(abs(self.denominator), abs(other.denominator))
        add_mul_self = nok // abs(self.denominator)
        add_mul_other = nok // abs(other.denominator)
        self.numerator *= add_mul_self
        other.numerator *= add_mul_other
        numerator = abs(self.numerator) + other.numerator
        return Fraction(sign * numerator, nok)

    def __str__(self):
        sign = '' if self.numerator * self.denominator > 0 else '-'
        numerator, denominator = abs(self.numerator), abs(self.denominator)
        k = math.gcd(numerator, denominator)
        numerator //= k
        denominator //= k
        if numerator == denominator:
            return f'1'
        if numerator > denominator:
            number = numerator // denominator
            remainder = numerator % denominator
            if not remainder:
                return f'{sign}{number}'
            return f'{sign}{number} {remainder}/{denominator}'
        return f'{sign}{numerator}/{denominator}'


if __name__ == '__main__':
    first = Fraction(3, 6)
    second = Fraction(4, -7)
    asd = first + second
    print(asd)
