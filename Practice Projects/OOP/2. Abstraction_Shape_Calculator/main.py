from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def describe(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        validate_lengths(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        validate_lengths(value, "height")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        return(f"Rectangle with width {self.width} and height {self.height}")


class Circle(Shape):
    pi = 3.14159
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        validate_lengths(value, "radius")
        self.__radius = value

    def area(self):
        return Circle.pi * (self.radius**2)

    def perimeter(self):
        return 2 * Circle.pi * self.radius

    def describe(self):
        return(f"Circle with radius {self.radius}")

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c

        #valid triangle
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("invalid triangle")

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        validate_lengths(value, "side_a")
        self.__side_a = value

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        validate_lengths(value, "side_b")
        self.__side_b = value

    @property
    def side_c(self):
        return self.__side_c

    @side_c.setter
    def side_c(self, value):
        validate_lengths(value, "side_c")
        self.__side_c = value

    def area(self):
        #semi-perimeter
        a = self.side_a
        b = self.side_b
        c = self.side_c
        s = (a + b + c) / 2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def describe(self):
        return(f"Triangle with sides {self.side_a}, {self.side_b}, {self.side_c}")

def validate_lengths(value, attribute):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{attribute} should be int or float")
    elif value <= 0:
        raise ValueError(f"{attribute} should be greater than 0")

def summarize_shape(shape):
    if not isinstance(shape, Shape):
        raise ValueError("invalid shape")
    return {
            "description": shape.describe(),
            "area": shape.area(),
            "perimeter": shape.perimeter()
        }

def main():
    # Shape Calculator tests

    rect = Rectangle(4, 5)

    assert rect.area() == 20
    assert rect.perimeter() == 18
    assert rect.describe() == "Rectangle with width 4 and height 5"

    circle = Circle(3)

    assert round(circle.area(), 2) == 28.27
    assert round(circle.perimeter(), 2) == 18.85
    assert circle.describe() == "Circle with radius 3"

    triangle = Triangle(3, 4, 5)

    assert triangle.perimeter() == 12
    assert round(triangle.area(), 2) == 6.00
    assert triangle.describe() == "Triangle with sides 3, 4, 5"

    summary = summarize_shape(rect)

    assert summary["description"] == "Rectangle with width 4 and height 5"
    assert summary["area"] == 20
    assert summary["perimeter"] == 18

    summary = summarize_shape(circle)

    assert summary["description"] == "Circle with radius 3"
    assert round(summary["area"], 2) == 28.27
    assert round(summary["perimeter"], 2) == 18.85

    summary = summarize_shape(triangle)

    assert summary["description"] == "Triangle with sides 3, 4, 5"
    assert round(summary["area"], 2) == 6.00
    assert summary["perimeter"] == 12

    try:
        Rectangle(0, 5)
        assert False
    except ValueError:
        assert True

    try:
        Rectangle(4, 0)
        assert False
    except ValueError:
        assert True

    try:
        Circle(-3)
        assert False
    except ValueError:
        assert True

    try:
        Circle(0)
        assert False
    except ValueError:
        assert True

    try:
        Triangle(1, 2, 10)
        assert False
    except ValueError:
        assert True

    try:
        Triangle(0, 4, 5)
        assert False
    except ValueError:
        assert True

    print("All Shape Calculator tests passed!")

if __name__ == "__main__":
    main()