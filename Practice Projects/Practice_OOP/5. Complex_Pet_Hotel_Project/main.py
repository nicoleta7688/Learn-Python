from pet import Pet
from booking import Booking
from pet_hotel import PetHotel

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