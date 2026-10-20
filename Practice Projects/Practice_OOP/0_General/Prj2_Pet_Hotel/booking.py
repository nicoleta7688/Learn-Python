from validators import validate_str
from pet import Pet

class Booking:
    def __init__(self, booking_id, pet, days):
        validate_str(booking_id, "booking_id")
        self.__booking_id = booking_id

        self.pet = pet
        self.days = days
        self.__status = 'active'

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def pet(self):
        return self.__pet
    # initialized only once, we don't need setter

    @pet.setter
    def pet(self, value):
        if not isinstance(value, Pet):
            raise TypeError(f"Pet should be an object of class Pet: {Pet}")
        self.__pet = value

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, value):
        if isinstance(value, bool) or not isinstance(value, int) :
            raise TypeError("days must be int")
        elif value <= 0:
            raise ValueError(f'days must be greater than 0')
        else:
            self.__days = value

    @property
    def status(self):
        return self.__status

    def cancel(self):
        if self.status == 'active':
            self.__status = 'cancelled'
        elif self.status == 'cancelled':
            raise ValueError("Reservation is already cancelled")

    def calculate_total(self):
        return self.pet.daily_rate * self.days

    def __str__(self):
        return (f'\n-----------------\n'
                f'Reservation Info:\n'
                f'ID: {self.booking_id}\n'
                f'Pet Name: {self.pet.name}\n'
                f'Species: {self.pet.species}\n'
                f'Days: {self.days}\n'
                f'Status: {self.status}\n'
                f'Total price: {self.calculate_total()}$\n'
                f'-----------------\n')
