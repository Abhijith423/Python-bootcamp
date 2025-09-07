#online laptop shop


class Laptop:
    def __init__(self,name,price,description,ram,ssd):
        self.name=name
        self.price=price
        self.description=description
        self.ram=ram
        self.ssd=ssd
    def spec(self):
        print(self.name + "has a powerful processor and a high resolution display.")
    def hi(self):
       print(self.name + "is the highest gross selling laptop in the market.")
    def details(self):
        print(self.name + "is a high-end laptop with a powerful processor and a high resolution display.")
        print(self.name + "Lap has an i7 processor")
        print(self.name + "Lap has a 16GB RAM")

lap1=Laptop("Dell Inspiron 15", 55000, "15.6-inch laptop with Intel i5", "8GB RAM", "512GB SSD")
lap2=Laptop("HP Pavilion", 45000, "14-inch laptop with AMD Ryzen 5", "16GB RAM", "256GB SSD")
lap3=Laptop("Lenovo ThinkPad E14", 75000, "Business laptop with Intel i7", "16GB RAM", "512GB SSD")
lap4=Laptop("Asus VivoBook 14", 48000, "Slim laptop with Ryzen 5", "8GB RAM", "512GB SSD")
lap5=Laptop("Apple MacBook Pro", 120000, "Powerful laptop with Apple M1 chip", "8GB RAM", "512GB SSD")
lap6=Laptop("Acer Aspire 5",45000, "Budget laptop with Intel i3", "8GB RAM", "1TB HDD")
lap7=Laptop("MSI GF63 Thin", 78000, "Gaming laptop with Intel i7", "16GB RAM", "GTX 1650 GPU")
lap8=Laptop("Razer Blade 15", 150000, "Premium gaming laptop with RTX 3060", "i7", "16GB RAM")
lap9=Laptop("Dell XPS 13", 120000, "Ultrabook with Intel i7", "16GB RAM", "512GB SSD")
lap10=Laptop("HP Omen 16", 110000, "Gaming laptop with Ryzen 7", "16GB RAM", "512GB SSD")
lap11=Laptop("Lenovo Legion 5", 95000, "Gaming laptop with Ryzen 7", "16GB RAM", "512GB SSD")
lap12=Laptop("Asus ROG Zephyrus G14", 135000, "Compact gaming laptop with Ryzen 9", "16GB RAM", "512GB SSD")
lap13=Laptop("Apple MacBook Pro 14", 180000, "Professional laptop with M1 Pro chip", "16GB RAM", "512GB SSD")
lap14=Laptop("Samsung Galaxy Book Flex", 85000, "2-in-1 laptop with Intel i7", "16GB RAM", "512GB SSD")
lap15=Laptop("Microsoft Surface Laptop 4", 115000, "Touchscreen laptop with Ryzen 5", "16GB RAM", "512GB SSD")
lap16=Laptop("LG Gram 16", 105000, "Ultra-light laptop with Intel i7", "16GB RAM", "1TB SSD")
lap17=Laptop("Acer Predator Helios 300", 125000, "High-performance gaming laptop with RTX 3060", "i7", "16GB RAM")
lap18=Laptop("HP EliteBook 840", 88000, "Business laptop with Intel i5", "16GB RAM", "512GB SSD")
lap19=Laptop("Dell Latitude 7410", 98000, "Enterprise laptop with Intel i7", "16GB RAM", "1TB SSD")
lap20=Laptop("Asus ZenBook 14", 85000, "Compact laptop with Intel i5", "8GB RAM", "512GB SSD")
lap21=Laptop("Lenovo Yoga Slim 7", 87000, "Slim ultrabook with Ryzen 7", "16GB RAM", "512GB SSD")

print(lap3.name, lap3.price)
