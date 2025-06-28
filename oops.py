#inheritance

class Car:
    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started")
class ElectricCar(Car):
    def charge_battery(self):
        print(f"{self.brand} {self.model} {self.year} model battery is charging")
my_car = ElectricCar("Toyota", "Corolla", 2022)
my_car.start_engine()
my_car.charge_battery()



       
   
