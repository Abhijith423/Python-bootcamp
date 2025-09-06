#employeee management system 
#oops python

            #employee management system in a company
class Ems:
    def __init__(self,name,id,department,salary,details):
        self.name=name
        self.id=id
        self.department=department
        self.salary=salary
        self.details=details
    def show_details(self):
        print(self.name+ "  has a working experience of 10yrs")

    def updated_salary(self):
        print(self.salary+    " has a salary 9000 per month")
    def updated_departement(self):
        print(self.department+  " has a department promoted to hr")
employee1=Ems('Adith',101,'Senior Analyst',10000,'has a 10yr experience')
employee2=Ems('Avesh',102,'Senior Analyst',20000,'has a 10yr experience')
employee1.name="aswin" #update name
employee2.department="HR"
print(employee2.department)
print(employee1.name)
employee1.show_details()
employee2.show_details()
