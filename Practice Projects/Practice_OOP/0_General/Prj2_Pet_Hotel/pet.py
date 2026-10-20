from validators import validate_str

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
            raise ValueError(f'species is not allowed')
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
            raise ValueError(f'daily_rate must be greater than 0')
        else:
            self.__daily_rate = float(value)

    def __str__(self):
        return f"ID: {self.pet_id}\nName: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nDaily rate: {self.daily_rate}"
