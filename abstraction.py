#abstraction
from abc  import ABC,abstractmethod
class Vehicle(ABC):
    def start(self):
        print("Start engine")
    def apply_brakes(self):
        print("Apply brakes")
    def stop(self):
        print("Stop engine")
    @abstractmethod
    def change_gear(self):
        pass
class Car(Vehicle):
    def sunroof(self):
        print("Open sunroof")
    def change_gear(self):
        print("Automatic Gear")
class Truck(Vehicle):
    def load(self):
        print("load weight")
    def change_gear(self):
        print("Change gear manually")

car1=Car()
car1.change_gear()
car1.sunroof()
car1.apply_brakes()

truck1=Truck()
truck1.change_gear()
truck1.load()
truck1.apply_brakes()
