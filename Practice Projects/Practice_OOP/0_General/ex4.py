#folosim dataclass, dar avem nevoie de validare - nu se merita data class

from dataclasses import dataclass

@dataclass(init=False)
class Product:
    name: str
    _price: float

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value