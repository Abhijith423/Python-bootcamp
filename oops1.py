#object oriented programing in python 

#oops python
#Cars

class Cars:
    def __init__(self,name,price,color):   #parameters
        self.name=name
        self.price=price   #name,price,color which are attributes
        self.color=color

    def start(self):    #methods
        print(self.name + "Engine Started")

car1=Cars("Maruti Dzire",120000,"red")
car2=Cars("Maruti Breeza",190000,"blue")

car2.price=15000
car2.color="white"

print(car1.name)
print(car2.name,car2.price,car2.color)

car1.start()




