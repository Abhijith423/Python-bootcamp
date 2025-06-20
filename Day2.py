#conditional statements and loops
u=96
if (int(u)>90):
    print("A Grade")
else:
    print("B Grade")

t=int(input("Enter a number:"))
if(int(t)>10):
    print("t is greater than 10")
elif(int(t)<10):
    print("t is less than 10")
else:
    print("t is equal to 10")

for i in range(0,10):
    print("hello")

while (i<=1):
    print("tt")

a=12,10
print(type(a))

b=[1,2,3,4,5]
print(b[1])
b.append(6)
print(b)

c={"name":"John", "age":30, "city":"New York"}
print(c)
print(c["age"])





