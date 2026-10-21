from pet import Pet
import pytest

@pytest.fixture
def pet():
    return Pet("P001", "Lola", "dog", 2, 2.5)

# -------------- pet_id tests --------------
def test_valid_pet_id(pet):
    assert pet.pet_id == 'P001'

@pytest.mark.parametrize("pet_id, expected_error, expected_message", [
    (31, TypeError, "pet_id must be string"),
    (None, TypeError, "pet_id must be string"),
    ('', ValueError, "pet_id cannot be empty"),
    ('   ', ValueError, "pet_id cannot be empty"),
])
def test_invalid_pet_id(pet_id, expected_error, expected_message):
    with pytest.raises(expected_error) as error:
        pet = Pet(pet_id, "Lola", "dog", 2, 2.5)

    assert str(error.value) == expected_message

def test_change_pet_id(pet):
    with pytest.raises(AttributeError):
        pet.pet_id = 'Lala'
    assert pet.pet_id == 'P001'
# ------------------------------------------


# --------------  name tests  --------------
invalid_name = [
    (31, TypeError, "name must be string"),
    (None, TypeError, "name must be string"),
    ('', ValueError, "name cannot be empty"),
    ('   ', ValueError, "name cannot be empty"),
]

@pytest.mark.parametrize("name", ['Lola', 'Lola Marie'])
def test_valid_name(pet, name):
    pet.name = name
    assert pet.name == name

@pytest.mark.parametrize("name, expected_error, expected_message", invalid_name)
def test_invalid_name(name, expected_error, expected_message):
    with pytest.raises(expected_error) as error:
        pet = Pet('P001', name, "dog", 2, 2.5)

    assert str(error.value) == expected_message

def test_change_name(pet):
    pet.name = 'ALOL'
    assert pet.name == 'ALOL'

@pytest.mark.parametrize("name, expected_error, expected_message", invalid_name)
def test_change_invalid_name(pet, name, expected_error, expected_message):
    with pytest.raises(expected_error) as error:
        pet.name = name

    assert str(error.value) == expected_message
    assert pet.name == 'Lola'
# ------------------------------------------

# --------------    species   --------------
invalid_species = [
    (31, TypeError, "species must be string"),
    (None, TypeError, "species must be string"),
    ('', ValueError, "species cannot be empty"),
    ('   ', ValueError, "species cannot be empty"),
    ('fox', ValueError, "species is not allowed"),
]

@pytest.mark.parametrize("species", ['dog', 'cat'])
def test_valid_species(pet, species):
    pet.species = species
    assert pet.species == species

@pytest.mark.parametrize("species, expected_error, expected_message", invalid_species)
def test_invalid_species(species, expected_error, expected_message):
    with pytest.raises(expected_error) as error:
        pet = Pet('P001', 'Lola', species, 2, 2.5)

    assert str(error.value) == expected_message

def test_change_species(pet):
    pet.species = 'cat'
    assert pet.species == 'cat'

@pytest.mark.parametrize("species, expected_error, expected_message", invalid_species)
def test_change_invalid_species(pet, species, expected_error, expected_message):
    with pytest.raises(expected_error) as error:
        pet.species = species

    assert str(error.value) == expected_message
    assert pet.species == 'dog'
# ------------------------------------------



# --------------      age     --------------
invalid_age = [
    (2.5, TypeError, "age must be int"),
    (None, TypeError, "age must be int"),
    ('2', TypeError, "age must be int"),
    (True, TypeError, "age must be int"),
    (-1, ValueError, "age must be between 0 and 30"),
    (31, ValueError, "age must be between 0 and 30"),
]

@pytest.mark.parametrize("age", [0, 30, 25])
def test_valid_age(pet, age):
    pet = Pet('P001', 'Lola', 'dog', age, 2.5)
    assert pet.age == age

@pytest.mark.parametrize("age, expected_error, expected_message", invalid_age)
def test_invalid_age(age, expected_error, expected_message):
    with pytest.raises(expected_error) as error:
        pet = Pet('P001', 'Lola', 'dog', age, 2.5)

    assert str(error.value) == expected_message

@pytest.mark.parametrize("age", [0, 30, 25])
def test_change_age(pet, age):
    pet.age = age
    assert pet.age == age

@pytest.mark.parametrize("age, expected_error, expected_message", invalid_age)
def test_change_invalid_age(pet, age, expected_error, expected_message):
    with pytest.raises(expected_error) as error:
        pet.age = age

    assert str(error.value) == expected_message
    assert pet.age == 2
# ------------------------------------------


# --------------  daily rate  --------------
invalid_daily_rate = [
    ('2.5', TypeError, "daily_rate must be float or int"),
    (None, TypeError, "daily_rate must be float or int"),
    (True, TypeError, "daily_rate must be float or int"),
    (-1.2, ValueError, "daily_rate must be greater than 0"),
    (0, ValueError, "daily_rate must be greater than 0"),
]

@pytest.mark.parametrize("daily_rate", [2, 2.5])
def test_valid_daily_rate(pet, daily_rate):
    pet = Pet('P001', 'Lola', 'dog', 2, daily_rate)
    assert pet.daily_rate == float(daily_rate)

@pytest.mark.parametrize("daily_rate, expected_error, expected_message", invalid_daily_rate)
def test_invalid_daily_rate(daily_rate, expected_error, expected_message):
    with pytest.raises(expected_error) as error:
        pet = Pet('P001', 'Lola', 'dog', 2, daily_rate)

    assert str(error.value) == expected_message

@pytest.mark.parametrize("daily_rate", [2, 2.5])
def test_change_daily_rate(pet, daily_rate):
    pet.daily_rate = daily_rate
    assert pet.daily_rate == float(daily_rate)

@pytest.mark.parametrize("daily_rate, expected_error, expected_message", invalid_daily_rate)
def test_change_invalid_daily_rate(pet, daily_rate, expected_error, expected_message):
    with pytest.raises(expected_error) as error:
        pet.daily_rate = daily_rate

    assert str(error.value) == expected_message
    assert pet.daily_rate == 2.5
# ------------------------------------------

def test_pet_str(pet):
        assert str(pet) == (
        f"ID: P001\n"
        f"Name: Lola\n"
        f"Species: dog\n"
        f"Age: 2\n"
        f"Daily rate: 2.5"
    )
