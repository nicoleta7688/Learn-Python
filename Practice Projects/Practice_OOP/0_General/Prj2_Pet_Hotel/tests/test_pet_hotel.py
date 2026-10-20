
import pytest

from pet import Pet
from booking import Booking
from pet_hotel import PetHotel


@pytest.fixture
def hotel():
    return PetHotel("Happy Paws")


@pytest.fixture
def pet():
    return Pet("P001", "Lola", "dog", 2, 25.0)


@pytest.fixture
def second_pet():
    return Pet("P002", "Milo", "cat", 1, 15.0)


@pytest.fixture
def booking(pet):
    return Booking("B001", pet, 3)


# Constructor and name

def test_valid_hotel(hotel):
    assert hotel.name == "Happy Paws"
    assert hotel.pets == []
    assert hotel.bookings == []


@pytest.mark.parametrize("name", [None, 123, [], {}])
def test_invalid_hotel_name_type(name):
    with pytest.raises(TypeError):
        PetHotel(name)


@pytest.mark.parametrize("name", ["", " ", "   "])
def test_empty_hotel_name(name):
    with pytest.raises(ValueError):
        PetHotel(name)


@pytest.mark.parametrize("name", ["New Hotel", "Pet Paradise"])
def test_valid_hotel_name(hotel, name):
    hotel.name = name
    assert hotel.name == name


# Pets

def test_add_pet(hotel, pet):
    hotel.add_pet(pet)

    assert len(hotel.pets) == 1
    assert hotel.pets[0] is pet


@pytest.mark.parametrize("invalid_obj", [None, "Lola", 123, [], {}])
def test_add_invalid_pet(hotel, invalid_obj):
    with pytest.raises(TypeError, match="instance of Pet"):
        hotel.add_pet(invalid_obj)


def test_add_duplicate_pet_id(hotel, pet):
    hotel.add_pet(pet)

    duplicate = Pet("P001", "Milo", "cat", 1, 15.0)

    with pytest.raises(ValueError, match="same id"):
        hotel.add_pet(duplicate)


def test_find_existing_pet(hotel, pet):
    hotel.add_pet(pet)

    assert hotel.find_pet("P001") is pet


def test_find_missing_pet(hotel):
    assert hotel.find_pet("UNKNOWN") is None


@pytest.mark.parametrize("pet_id", [None, 123, [], {}])
def test_find_pet_invalid_id_type(hotel, pet_id):
    with pytest.raises(TypeError):
        hotel.find_pet(pet_id)


@pytest.mark.parametrize("pet_id", ["", " ", "   "])
def test_find_pet_empty_id(hotel, pet_id):
    with pytest.raises(ValueError):
        hotel.find_pet(pet_id)


def test_pets_property_returns_copy(hotel, pet):
    hotel.add_pet(pet)

    pets = hotel.pets
    pets.clear()

    assert len(hotel.pets) == 1


# Bookings

def test_add_booking(hotel, pet, booking):
    hotel.add_pet(pet)
    hotel.add_booking(booking)

    assert len(hotel.bookings) == 1
    assert hotel.bookings[0] is booking


@pytest.mark.parametrize("invalid_obj", [None, "booking", 123, [], {}])
def test_add_invalid_booking(hotel, invalid_obj):
    with pytest.raises(TypeError, match="instance of Booking"):
        hotel.add_booking(invalid_obj)


def test_add_duplicate_booking_id(hotel, pet, booking):
    hotel.add_pet(pet)
    hotel.add_booking(booking)

    duplicate = Booking("B001", pet, 5)

    with pytest.raises(ValueError, match="same id"):
        hotel.add_booking(duplicate)


def test_cannot_add_booking_for_unregistered_pet(hotel, booking):
    with pytest.raises(ValueError, match="isn't registred"):
        hotel.add_booking(booking)


def test_find_existing_booking(hotel, pet, booking):
    hotel.add_pet(pet)
    hotel.add_booking(booking)

    assert hotel.find_booking("B001") is booking


def test_find_missing_booking(hotel):
    assert hotel.find_booking("UNKNOWN") is None


@pytest.mark.parametrize("booking_id", [None, 123, [], {}])
def test_find_booking_invalid_id_type(hotel, booking_id):
    with pytest.raises(TypeError):
        hotel.find_booking(booking_id)


@pytest.mark.parametrize("booking_id", ["", " ", "   "])
def test_find_booking_empty_id(hotel, booking_id):
    with pytest.raises(ValueError):
        hotel.find_booking(booking_id)


def test_bookings_property_returns_copy(hotel, pet, booking):
    hotel.add_pet(pet)
    hotel.add_booking(booking)

    bookings = hotel.bookings
    bookings.clear()

    assert len(hotel.bookings) == 1


# Revenue

def test_revenue_with_one_active_booking(hotel, pet, booking):
    hotel.add_pet(pet)
    hotel.add_booking(booking)

    assert hotel.calculate_revenue() == pytest.approx(75.0)


def test_cancelled_booking_not_in_revenue(hotel, pet, booking):
    hotel.add_pet(pet)
    hotel.add_booking(booking)
    booking.cancel()

    assert hotel.calculate_revenue() == 0


def test_revenue_with_multiple_bookings(hotel, pet, second_pet):
    hotel.add_pet(pet)
    hotel.add_pet(second_pet)

    booking1 = Booking("B001", pet, 3)       # 25 * 3 = 75
    booking2 = Booking("B002", second_pet, 4)  # 15 * 4 = 60

    hotel.add_booking(booking1)
    hotel.add_booking(booking2)

    assert hotel.calculate_revenue() == pytest.approx(135.0)


def test_revenue_excludes_only_cancelled_bookings(
    hotel, pet, second_pet
):
    hotel.add_pet(pet)
    hotel.add_pet(second_pet)

    booking1 = Booking("B001", pet, 3)
    booking2 = Booking("B002", second_pet, 4)

    hotel.add_booking(booking1)
    hotel.add_booking(booking2)
    booking1.cancel()

    assert hotel.calculate_revenue() == pytest.approx(60.0)


def test_revenue_without_bookings(hotel):
    assert hotel.calculate_revenue() == 0


# String representation

def test_hotel_str_without_pets_or_bookings(hotel):
    expected = (
        "\n-----------------\n"
        "Hotel Info:\n"
        "Hotel's name: Happy Paws\n"
        "Nr. of animals: 0\n"
        "Nr. of total bookings: 0\n"
        "Nr. of active bookings: 0\n"
        "-----------------\n"
    )

    assert str(hotel) == expected


def test_hotel_str_with_active_and_cancelled_bookings(
    hotel, pet, second_pet
):
    hotel.add_pet(pet)
    hotel.add_pet(second_pet)

    booking1 = Booking("B001", pet, 3)
    booking2 = Booking("B002", second_pet, 4)

    hotel.add_booking(booking1)
    hotel.add_booking(booking2)
    booking2.cancel()

    result = str(hotel)

    assert "Nr. of animals: 2" in result
    assert "Nr. of total bookings: 2" in result
    assert "Nr. of active bookings: 1" in result
