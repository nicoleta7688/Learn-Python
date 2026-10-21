#Practice inheritance & polymorphism

class Vehicle:
    def __init__(self, brand, daily_rate):
        self.brand = brand
        self.daily_rate = daily_rate

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise TypeError("brand must be str")
        elif value.strip() == '':
            raise ValueError("brand cannot be empty")
        self.__brand = value

    @property
    def daily_rate(self):
        return self.__daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("daily_rate must be int or float")
        elif value <= 0:
            raise ValueError("daily_rate must be greater than 0")
        self.__daily_rate = value

    def calculate_rental(self, days):
        validate_int(days, "days")
        return self.daily_rate * days

    def display_info(self):
        return f"Brand: {self.brand}\nDaily rate: {self.daily_rate}$"

    def __str__(self):
        return self.display_info()


class Car(Vehicle):
    type = 'Car'
    def __init__(self, brand, daily_rate, number_of_doors):
        super().__init__(brand, daily_rate)
        self.number_of_doors = number_of_doors

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, value):
        validate_int(value, "number_of_doors")
        self.__number_of_doors = value

    def display_info(self):
        base = super().display_info()
        return base + "\nNr. of doors: " + str(self.number_of_doors)

    def __str__(self):
        return self.type + ':\n' + super().__str__()


class Motorcycle(Vehicle):
    type = 'Motorcycle'
    # def __init__(self, brand, daily_rate):
    #     super().__init__(brand, daily_rate)

    def __str__(self):
        return self.type + ':\n' + super().__str__()


def validate_int(value, attribute):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{attribute} must be int")
    elif value <= 0:
        raise ValueError(f"{attribute} must be greater than 0")

def main():
    v1 = Vehicle("Mercedes", 2.5)

    print(v1)

    # v1.brand = 2
    # v1.brand = '  '
    # v1.daily_rate = -2
    # v1.daily_rate = True

    c1 = Car("Porsche", 2.5, 4)
    m1 = Motorcycle("ceva", 1)

    #This is polymorphism - when we have the same method for multiple objects from different classes, but it behaves differently:
    print(c1)
    print(m1)


if __name__ == "__main__":
    main()