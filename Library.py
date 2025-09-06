    # Digital Library system


class Lbs:
    def __init__(self,name,id,price):
        self.name=name
        self.id=id
        self.price=price
    def addbook(self):
        print(self.name+ " is the highest selling book in this library")
    def pricebook(self):
        print(self.name + " is the high costly book in the library")


book1=Lbs('Goosebumbs',202,1780)
book2=Lbs('Sdg',243,2760)
book3=Lbs('Efg',245,3890)
print(book1.name,book1.id,book1.price)
print(book2.name,book2.id,book2.price)
book1.addbook()
book2.pricebook()
