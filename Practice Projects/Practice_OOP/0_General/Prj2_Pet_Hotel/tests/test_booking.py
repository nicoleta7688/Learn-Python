
import pytest

from pet import Pet
from booking import Booking

@pytest.fixture
def pet():
    return Pet("P001", "Lola", "dog", 2, 25.0)


@pytest.fixture
def booking(pet):
    return Booking("B001", pet, 3)


# Constructor

def test_valid_booking(booking, pet):
    assert booking.booking_id == "B001"
    assert booking.pet is pet
    assert booking.days == 3
    assert booking.status == "active"


@pytest.mark.parametrize("booking_id", [None, 123, [], {}])
def test_invalid_booking_id_type(pet, booking_id):
    with pytest.raises(TypeError):
        Booking(booking_id, pet, 3)


@pytest.mark.parametrize("booking_id", ["", " ", "   "])
def test_empty_booking_id(pet, booking_id):
    with pytest.raises(ValueError):
        Booking(booking_id, pet, 3)


@pytest.mark.parametrize("invalid_pet", [None, "Lola", 123, [], {}])
def test_invalid_pet_type(invalid_pet):
    with pytest.raises(TypeError):
        Booking("B001", invalid_pet, 3)


# Days validation

@pytest.mark.parametrize("days", [0, -1, -10])
def test_invalid_days_value(pet, days):
    with pytest.raises(ValueError, match="days must be greater than 0"):
        Booking("B001", pet, days)


@pytest.mark.parametrize("days", [True, False, 1.5, "3", None, [], {}])
def test_invalid_days_type(pet, days):
    with pytest.raises(TypeError, match="days must be int"):
        Booking("B001", pet, days)


@pytest.mark.parametrize("days", [1, 2, 10, 365])
def test_valid_days(booking, days):
    booking.days = days
    assert booking.days == days


# Property validation

def test_booking_id_is_read_only(booking):
    with pytest.raises(AttributeError):
        booking.booking_id = "B002"


def test_status_is_read_only(booking):
    with pytest.raises(AttributeError):
        booking.status = "cancelled"


def test_pet_setter_accepts_pet(booking):
    new_pet = Pet("P002", "Milo", "cat", 1, 15.0)
    booking.pet = new_pet
    assert booking.pet is new_pet


def test_pet_setter_rejects_invalid_object(booking):
    with pytest.raises(TypeError):
        booking.pet = "Milo"


# Cancellation

def test_cancel_active_booking(booking):
    booking.cancel()
    assert booking.status == "cancelled"


def test_cancel_already_cancelled_booking(booking):
    booking.cancel()

    with pytest.raises(ValueError, match="already cancelled"):
        booking.cancel()


# Total price

@pytest.mark.parametrize(
    ("daily_rate", "days", "expected"),
    [
        (25.0, 3, 75.0),
        (10.0, 1, 10.0),
        (12.5, 4, 50.0),
        (99.0, 10, 990.0),
    ],
)
def test_calculate_total(daily_rate, days, expected):
    pet = Pet("P001", "Lola", "dog", 2, daily_rate)
    booking = Booking("B001", pet, days)

    assert booking.calculate_total() == pytest.approx(expected)


# String representation

def test_booking_str(booking):
    expected = (
        "\n-----------------\n"
        "Reservation Info:\n"
        "ID: B001\n"
        "Pet Name: Lola\n"
        "Species: dog\n"
        "Days: 3\n"
        "Status: active\n"
        "Total price: 75.0$\n"
        "-----------------\n"
    )

    assert str(booking) == expected


def test_booking_str_after_cancellation(booking):
    booking.cancel()
    assert "Status: cancelled" in str(booking)
