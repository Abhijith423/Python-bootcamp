    #Inheritance Cars
class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def addr(self):
        print(self.name,self.price)

class Luxury(Car):
    pass
class Nonlux(Car):
    pass

car1=Luxury("Benz",10000000)
car2=Nonlux("Scorpio",3000000)
car3=Luxury("Audi",10000000)
car4=Luxury("Ferrari",3000000)
car5=Nonlux("volkswagen vento",1800000)
car1.addr()
car2.addr()
car3.addr()
car4.addr()
car5.addr()
