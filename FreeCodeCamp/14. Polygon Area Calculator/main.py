import math 

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        if not isinstance(width, int) or not isinstance(height, int):
            raise ValueError("Width and Height must be int")
        self.width = width
        self.height = height

    def set_width(self, new_width: int) -> None:
        if not isinstance(new_width, int):
            raise ValueError("Width must be int")
        self.width = new_width

    def set_height(self, new_height: int) -> None:
        if not isinstance(new_height, int):
            raise ValueError("Height must be int")
        self.height = new_height

    def get_area(self) -> float:
        return self.height * self.width
    
    def get_perimeter(self) -> int:
        return 2 * (self.height + self.width)
    
    def get_diagonal(self) -> float:
        # return math.hypot(self.width, self.height)
        return math.sqrt(pow(self.height, 2) + pow(self.width, 2))
    
    def get_picture(self) -> str:
        pic_str = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        for h in range(self.height):
            for w in range(self.width):
                pic_str += '*'
            pic_str += '\n'

        return pic_str

    def get_amount_inside(self, shape) -> int:
        return ((self.width // shape.width) * (self.height // shape.height))

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    
    def set_width(self, new_length: int) -> None:
        if not isinstance(new_length, int):
            raise ValueError("Lenght must be int")
        self.width = new_length
        self.height = new_length

    def set_height(self, new_length: int) -> None:
        if not isinstance(new_length, int):
            raise ValueError("Lenght must be int")
        self.width = new_length
        self.height = new_length

    def set_side(self, new_length: int) -> None:
        if not isinstance(new_length, int):
            raise ValueError("Lenght must be int")
        self.width = new_length
        self.height = new_length

    def __str__(self):
        return f"Square(side={self.height})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
