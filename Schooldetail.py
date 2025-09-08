
class School:
    def __init__(self,name,department,college):
        self.name=name
        self.department=department
        self.college=college
    def display(self):
        print(self.name,self.department,self.college)

class Student(School):
    pass
class Teacher(School):
    pass
class Staff(School):
    pass

std1=Student("Adith","Computer Science","TKM")
teacher=Teacher("Hari","Computer Science","TKM")
staff=Staff("John","Computer Science","TKM")

std1.display()
teacher.display()
staff.display()
