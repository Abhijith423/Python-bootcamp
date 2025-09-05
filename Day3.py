#functions define
from audioop import avg
def greet():
    print("good morning Everyone")
#function call
for i in range(1,6):
    greet()
#function with arguement
def total(a,b):
    return a+b
print(total(10,20))
#average
def total(a=10,b=20):
    return a+b
z=(total(4))
avg=z/2
print(avg)
#Area of the rectangel
def area(l=10,b=20):
    print("Area of the rectangle",l*b)
area(7,8)

def area(l=10,b=20):
    print("Area of the rectangle",l*b)
area()

def home():
    print("Hello")
home()
home()

def message(name):
    print("Hello " + name)
message("Anil")
message("John")

def sum(a,b):
    print(a+b)
sum(2,3)

def msg():
    return "hello"
print(msg())

def sqrt(n):
    return n*n
print(sqrt(5))

#Strings
str="hello world"
print(str[7])
print(str[7:4:-1])

x="HelloWorld"
print(x.upper())
print(x.lower())
print(x.strip())
print(len(x))

x="Hello How are You"
print(x.split())

#Split the Contact no code
contactno="+94-1234567890"
print(contactno.split("-"))

#List Comprehension
cubes=[i**3 for i in range(1,6)]
cubes.append(i*i*i*i)
print(cubes)

marks=[45,56,78,90,19]

for mark in marks:
    if mark>=40:
        print("pass")
    elif mark<40:
        print("fail")
    else:
        print("Malpractice")

print(marks[4])

for i in range(100):
    print(i)





