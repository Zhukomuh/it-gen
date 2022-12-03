import time


class Timber:
    def __init__(self, species: str, height: int, width: int, length: int, price: float):
        self.species = species
        self.height = height
        self.width = width
        self.length = length
        self.price = price

    def __str__(self):
        return f"{self.species.title()} wood\n{'=' * 20}\nHeight: {self.height}\nWidth: {self.width}\nLength:" \
               f" {self.length}\nPrice: {self.price} $"


class Buyer:
    def __init__(self, name: str, lastname: str, mobile: str):
        self.name = name
        self.lastname = lastname
        self.mobile = mobile

    def __str__(self):
        return f"{self.name.title()} {self.lastname.title()}\n{'=' * 20}\nMobile Phone: {self.mobile}"


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.check = []
        self.total = 0

    def add_order(self, article, quantity):
        self.check.append(f'{str(article)}\nQuantity={quantity}\nSum={article.price * quantity}$')
        self.total += article.price * quantity

    def __str__(self):
        return f"{time.asctime(time.localtime())}\n{'=' * 20}\n{self.customer}\n{'=' * 20}\n" + \
               '\n'.join(map(str, self.check)) + f'\nTotal: {self.total}$'


oak_wood = Timber('oak', 100, 50, 500, 135.50)
pine_wood = Timber('pine', 75, 60, 600, 200.0)
alex = Buyer('Olexander', 'Holosenko', '+380955253304')
alex_order = Order(alex)
alex_order.add_order(oak_wood, 20)
alex_order.add_order(pine_wood, 10)
print(alex_order)
