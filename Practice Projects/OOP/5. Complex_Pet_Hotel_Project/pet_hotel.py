from validators import validate_str
from pet import Pet
from booking import Booking

class PetHotel:
    def __init__(self, name):
        self.name = name
        self.__pets = []
        self.__bookings = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_str(value, "name")
        self.__name = value

    @property
    def pets(self):
        return self.__pets.copy()
    
    @property
    def bookings(self):
        return self.__bookings.copy()

    def add_pet(self, obj):
        if not isinstance(obj, Pet):
            raise TypeError("obj should be an instance of Pet")
        for pet in self.pets:
            if obj.pet_id == pet.pet_id:
                raise ValueError("obj with the same id is already added")
        self.__pets.append(obj)

    def find_pet(self, obj_id):
        validate_str(obj_id, "id")

        for pet in self.pets:
            if obj_id == pet.pet_id: 
                return pet
        return None

    def add_booking(self, obj):
        if not isinstance(obj, Booking):
            raise TypeError("obj should be an instance of Booking")
        for item in self.bookings:
            if obj.booking_id == item.booking_id:
                raise ValueError("obj with the same id is already added")

        if obj.pet in self.pets:
            self.__bookings.append(obj)
        else:
            raise ValueError("pet isn't registred in hotel")

    def find_booking(self, obj_id):
        validate_str(obj_id, "id")

        for item in self.bookings:
            if obj_id == item.booking_id: 
                return item
        return None

    def calculate_revenue(self):
        total = 0
        for item in self.bookings:
            if item.status == "active":
                total += item.calculate_total()
        return total

    def __str__(self):
        active_bookings = 0
        for booking in self.bookings:
            if booking.status == 'active':
                active_bookings += 1

        return (f'\n-----------------\n'
                f'Hotel Info:\n'
                f"Hotel's name: {self.name}\n"
                f"Nr. of animals: {len(self.pets)}\n"
                f"Nr. of total bookings: {len(self.bookings)}\n"
                f"Nr. of active bookings: {active_bookings}\n"
                f'-----------------\n')
