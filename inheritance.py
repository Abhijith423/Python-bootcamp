    #Inheritance hospital system

class Person: #parent class
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

    def addr(self):
        print(self.name,self.contact)

class Doctor(Person):#child class
    pass
class Patient(Person):#child class
    pass

doc1=Doctor("Dr. Smith", "123-456-7890")
pat1=Patient("John Doe", "555-123-4567")

doc1.addr()
pat1.addr()
