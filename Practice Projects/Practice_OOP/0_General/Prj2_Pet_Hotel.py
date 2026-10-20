GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

def validate_str(value, arg):
    if not isinstance(value, str):
        raise TypeError(f"{arg} must be string")
    elif value.strip() == "":
        raise ValueError(f"{arg} cannot be empty")

class Pet:
    accepted_animals = ("dog", "cat") #tuple used because we want to be immutable
    def __init__(self, pet_id, name, species, age, daily_rate):
        validate_str(pet_id, "pet_id")
        self.__pet_id = pet_id
        self.name = name
        self.species = species
        self.age = age
        self.daily_rate = daily_rate

    @property
    def pet_id(self):
        return self.__pet_id
    # initialized only once, we don't need setter


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_str(value, "name")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        validate_str(value, "species")
        if value not in self.accepted_animals:
            raise ValueError(f'species isn\'t allowed. Accepted species are: {", ".join(self.accepted_animals)}')
        else:
            self.__species = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, bool) or not isinstance(value, int) :
            raise TypeError("age must be int")
        elif not 0 <= value <= 30:
            raise ValueError(f'age must be between 0 and 30')
        else:
            self.__age = value

    @property
    def daily_rate(self):
        return self.__daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        if isinstance(value, bool) or not isinstance(value, (float, int)):
            raise TypeError("daily_rate must be float or int")
        elif value <= 0:
            raise ValueError(f'daily_rate must be positive')
        else:
            self.__daily_rate = float(value)

    def __str__(self):
        return f"ID: {self.pet_id}\nName: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nDaily rate: {self.daily_rate}"

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


def format_arg(value):
    if isinstance(value, (Pet, Booking)):
        return f"<{type(value).__name__} object>"
    return repr(value)

def try_create_obj(arg, class_type, test_description, expect_error = True):
    if not hasattr(try_create_obj, "counter"):
        try_create_obj.counter = 1

    print(f"Test nr.{try_create_obj.counter}: {test_description}")

    try:
        if class_type == 'Pet':
            print("obj = Pet(pet_id, name, species, age, daily_rate)")
            print(f"obj = {class_type}({", ".join(map(format_arg, arg))})")
            obj = Pet(*arg)
        elif class_type == "Booking":
            print("obj = Booking(bookig_id, pet, days)")
            print(f"obj = {class_type}({", ".join(map(format_arg, arg))})")
            obj = Booking(*arg)
        elif class_type == 'PetHotel':
            print("obj = PetHotel(name)")
            print(f"obj = {class_type}({arg})")
            obj = PetHotel(arg)
    except (ValueError, TypeError) as e:
        print(e)
        if expect_error:
            print(f"{GREEN}Passed successful{RESET}")
        else:
            print(f"{RED}Test Failed!{RESET}")
    else:
        if expect_error:
            print(f"{RED}Attention! Object was created{RESET}")
        else:
            print(f"{GREEN}Passed successful{RESET}")
            print(f"Object was created successful")
        del obj
        print(f"Object automatically deleted!")
    finally:
        print()
        try_create_obj.counter += 1

def test_arguments():
    pet_obj = Pet("Test1", "Barni", "dog", 2, 2.5)
    booking_obj = Booking("Test2", pet_obj, 3)

    class_type = "Pet"
    print(f"Tests for {class_type} class")
    # ======== pet_id tests: 
    try_create_obj([1, "Lola", "dog", 2, 2.5], class_type, test_description = "pet_id - not str")
    try_create_obj(["", "Lola", "dog", 2, 2.5], class_type, test_description = "pet_id - is empty")
    try_create_obj(["    ", "Lola", "dog", 2, 2.5], class_type, test_description = "pet_id - have only trailing spaces")

    # ======== name tests:
    try_create_obj(["P001", 22, "dog", 2, 2.5], class_type, test_description = "name - not str")
    try_create_obj(["P001", "", "dog", 2, 2.5], class_type, test_description = "name - is empty")
    try_create_obj(["P001", "   ", "dog", 2, 2.5], class_type, test_description = "name - have only trailing spaces")

    # ======== species tests:
    try_create_obj(["P001", "Lola", 22, 2, 2.5], class_type, test_description = "species - not str")
    try_create_obj(["P001", "Lola", "", 2, 2.5], class_type, test_description = "species - empty")
    try_create_obj(["P001", "Lola", "bird", 2, 2.5], class_type, test_description = "species - not dog or cat")

    # ======== age tests:
    try_create_obj(["P001", "Lola", "dog", "2", 2.5], class_type, test_description = "age - not int")
    try_create_obj(["P001", "Lola", "dog", 200, 2.5], class_type, test_description = "age - not in limits")
    try_create_obj(["P001", "Lola", "dog", True, 2.5], class_type, test_description = "age - bool value") 

    # ======== daily_rate tests:
    try_create_obj(["P001", "Lola", "dog", 2, '2.5'], class_type, test_description = "daily_rate - not float")
    try_create_obj(["P001", "Lola", "dog", 2, 2], class_type, test_description = "daily_rate - is int - should work", expect_error = False)
    try_create_obj(["P001", "Lola", "dog", 2, -2.5], class_type, test_description = "daily_rate - < 0")

    class_type = "Booking"
    print(f"Tests for {class_type} class")

    # ======== booking_id tests: 
    try_create_obj([2, pet_obj, 3], class_type, test_description = "booking_id - not str")
    try_create_obj(["", pet_obj, 3], class_type, test_description = "booking_id - is empty")
    try_create_obj(["    ", pet_obj, 3], class_type, test_description = "booking_id - have only trailing spaces")

    # ======== pet tests: 
    try_create_obj(["B001", "Pet", 3], class_type, test_description = "pet - not Pet")
    try_create_obj(["B001", booking_obj, 3], class_type, test_description = "pet - another object type")

    # ======== days tests:
    try_create_obj(["B001", pet_obj, 3.2], class_type, test_description = "days - not int")
    try_create_obj(["B001", pet_obj, 0], class_type, test_description = "days - is 0")
    try_create_obj(["B001", pet_obj, -10], class_type, test_description = "days - negative nr")
    try_create_obj(["B001", pet_obj, True], class_type, test_description = "days - bool value") # !!!bool is a subclass of int!!!


    class_type = "PetHotel"
    # ======== name tests:
    try_create_obj(12, class_type, test_description = "name - not str")
    try_create_obj("   ", class_type, test_description = "name - is empty")
    try_create_obj("    ", class_type, test_description = "name - have only trailing spaces")
    try_create_obj("Name", class_type, test_description = "name - correct form", expect_error = False)

def test_booking_methods(pet1, booking1):
    print(booking1.calculate_total())
    
    pet1.daily_rate = 4
    print(booking1.calculate_total())

    booking1.cancel()
    print(booking1)

    try:
        booking1.cancel()
    except ValueError as e:
        print(e)

    try:
        booking1.days = 0
    except ValueError as e:
        print(e)

def test_pet_hotel_methods(hotel1, pet1, pet2, booking1,  booking2):
    try:
        hotel1.add_pet(booking1)
    except TypeError as e:
        print(e)

    try:
        hotel1.add_pet(pet1)
    except ValueError as e:
        print(e)


    print(hotel1)

    print(hotel1.find_pet("P001"))

    print(hotel1.find_pet("P9"))

    hotel1.add_booking(booking1)

    try:
        hotel1.add_booking(booking2)
    except ValueError as e:
        print(e)

    print(hotel1.find_booking("B001"))

    print(hotel1.find_booking("P9"))

    print(hotel1.calculate_revenue())

    hotel1.add_pet(pet2)
    hotel1.add_booking(booking2)

    print(hotel1.calculate_revenue())

    pet3 = Pet("P003", "Daizy", "dog", 2, 3)
    booking3 = Booking("B003", pet3, 6)
    hotel1.add_pet(pet3)
    hotel1.add_booking(booking3)
    print(hotel1.calculate_revenue())

    booking3.cancel()
    print(hotel1.calculate_revenue())



def main():
    test_arguments()

    pet1 = Pet("P001", "Lola", "dog", 2, 2.5)
    pet2 = Pet("P002", "Barni", "dog", 2, 3)


    booking1 = Booking("B001", pet1, 3)
    booking2 = Booking("B002", pet2, 6)

    hotel1 = PetHotel("Leta's Pet Hotel")
    hotel1.add_pet(pet1)

    # print(pet1)
    test_booking_methods(pet1, booking1) #Test Booking Methods

    test_pet_hotel_methods(hotel1, pet1, pet2, booking1, booking2) # Test PetHotel Methods

    try:
        pet1.pet_id = 'hahs'
    except AttributeError as e:
        print(e)

if __name__ == "__main__":
    main()