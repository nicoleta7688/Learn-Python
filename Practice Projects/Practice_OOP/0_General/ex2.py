class Temperature:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, temp):
        if temp < -50 or temp > 60:
            raise ValueError("Temperature must be between -50 and 60")
        self.__value = temp

t1 = Temperature(22)
print(t1.value)
t1.value = 30
print(t1.value)

t1.__value = 100
print(t1.__value) #Python creează un atribut separat, numit literalmente __value
print(t1.value)  #devine _Temperature__value