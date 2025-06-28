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


#polymorphism

class car:
    def fuel_type(self):
        print("Petrol,diesel or CNG")
class ElectricCar(car):
    def fuel_type(self):
        print("Electric or Hybrid")
my_car=car()
my_car.fuel_type()
my_car=ElectricCar()
my_car.fuel_type()

#duck typing in Python

class Dog:
    def speak(self):
        print("Bark")
class cat:
    def speak(self):
        print("Meow")
class tiger:
    def speak(self):
        print("Roar")
def make_sound(animal):
    animal.speak()
make_sound(Dog())
make_sound(cat())
make_sound(tiger())



       
   



       
   
