from abc import ABC,  abstractmethod

class SmartDevice(ABC):
    def __init__(self, name, device_id):
        self.name = name
        self.device_id =  device_id
        self.__is_on = False  #encapsulation

    @property
    def is_on(self):
        return self.__is_on

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    @abstractmethod # abstraction
    def get_status(self):
        pass

    def __str__(self):
        return f'{self.name}({self.device_id})'

class Light(SmartDevice): # inherintance
    def __init__(self, name, device_id, brightness):
        super().__init__(name, device_id)
        self.brightness = brightness

    def get_status(self):
        if self.is_on:
            return f"{self.name} is ON — brightness: {self.brightness}%"
        else:
            return f"{self.name} is OFF"


class Thermostat(SmartDevice):
    def __init__(self, name, device_id, temperature):
        super().__init__(name, device_id)
        self.temperature = temperature

    def get_status(self):
        if self.is_on:
            return f"{self.name} is ON — temperature: {self.temperature}°C"
        else:
            return f"{self.name} is OFF"


class SmartLock(SmartDevice):
    def __init__(self, name, device_id, locked):
        super().__init__(name, device_id)
        self.locked = locked

    def get_status(self):
        if self.is_on:
            return f"{self.name} is ON - locked" if self.locked else f"{self.name} is ON - unlocked"
        else:
            return f"{self.name} is OFF"

class SmartHome():
    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def show_all_statuses(self):
        #polymorphysm
        return "\n".join(device.get_status() for device in self.devices)

    def turn_all_on(self):
        for device in self.devices:
            device.turn_on()

    def turn_all_off(self):
        for device in self.devices:
            device.turn_off()

    def __str__(self):
        devices_names = []
        for device in self.devices:
            devices_names.append(device.name)

        return f'Smart devices in {self.name}: {", ".join(devices_names)}'

def main():
    light1  = Light("Living Room Light", "L001", 80)
    thermostat1  = Thermostat("Thermostat", "T001", 23)
    smartlock1 = SmartLock("Front Door", "S001", True)
    smarthome1 = SmartHome("Leta's home")

    smarthome1.add_device(light1)
    smarthome1.add_device(thermostat1)
    smarthome1.add_device(smartlock1)

    print(smarthome1)

    print(smarthome1.show_all_statuses())
    smarthome1.turn_all_on()
    print(smarthome1.show_all_statuses())

    #polymorphysm: get_status()
    # print(light1.get_status())
    # light1.turn_on()
    # print(light1.get_status())

    # print(thermostat1.get_status())
    # thermostat1.turn_on()
    # print(thermostat1.get_status())

    # print(smartlock1.get_status())
    # smartlock1.turn_on()
    # print(smartlock1.get_status())
    # smartlock1.locked = False
    # print(smartlock1.get_status())

if __name__ == "__main__":
    main()