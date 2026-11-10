from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"

ph = PHSensor()
temp = TempSensor()

print("--- Lab Inventory System ---")
print(f"[pH Sensor] Reading: {ph.get_reading()}")
print(f"[Temperature Sensor] Reading: {temp.get_reading()}")
print("----------------------------")

# Task 5: Try creating an object directly from Sensor
my_sensor = Sensor()