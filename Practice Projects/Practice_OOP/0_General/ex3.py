#exemplu cu data class, cand nu avem nevoie de validare dupa intializare

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("Prețul trebuie să fie pozitiv!")



#exemplu cu classVar - cand vrem intr-un data class sa avem un atribut de clasa

from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Product:
    name: str
    price: float

    categories: ClassVar[list[str]] = ["BOOK", "GAME", "TOY"]