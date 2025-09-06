#oops python

class Vegetables:

    def __init__(self,name,price):  #init is aconstructor
        self.name=name
        self.price=price=price

    def start(self):                #method
        print(self.name+"Eating Started")

veg1=Vegetables("cabbage",50)    #objecname=classname(values)
veg2=Vegetables("Brocholi",45)
veg3=Vegetables("Potato",60)

veg2.name="cauliflower"

print(veg2.name,veg2.price)
printf()

veg2.start() #call a method
