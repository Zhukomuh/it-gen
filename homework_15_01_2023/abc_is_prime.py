import abc


class AbstractIsPrime(abc.ABC):
    """ABC class with an abstract method
    of checking if an integer is prime."""
    @abc.abstractmethod
    def is_prime(self, num):
        pass


class TestIsPrime(AbstractIsPrime):
    """Class inheriting AbstractIsPrime ABC class"""
    def is_prime(self, num):
        if num <= 1:
            return False
        for x in range(2, num):
            if num % x == 0:
                return False
        return True


class AnotherTestIsPrime:
    """class that does not inherit from a
     AbstractIsPrime ABC class, but has the necessary method."""
    @staticmethod
    def is_prime(num):
        if num <= 1:
            return False
        for x in range(2, num):
            if num % x == 0:
                return False
        return True


if __name__ == '__main__':
    AbstractIsPrime.register(AnotherTestIsPrime)
    test1 = AnotherTestIsPrime()
    test2 = TestIsPrime()
    print(isinstance(test1, AbstractIsPrime))
    print(test1.is_prime(3))
    print(test2.is_prime(3))
