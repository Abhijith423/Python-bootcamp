#class variables

class Student:

    class_year = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Aaron", 20)
student2 = Student("Janvi", 21)

print(student1.name,student1.age)
print(student2.name,student2.age)
print(Student.class_year)
