class Electronics:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Electronic device name",self.name)
class Mobiledevice(Electronics):
    def __init__(self, name,brand):
        super().__init__(name)
        self.brand=brand
    def display(self):
        print(f"Mobile device name {self.name} and brand {self.brand}")
class Smartphone(Mobiledevice):
    def __init__(self, name, brand,year):
        super().__init__(name, brand)
        self.year=year
    def display(self):
        print(f"Smartphone name {self.name} and brand {self.brand} and year {self.year}")

smartphone=Smartphone('Galaxy 22','Samsung',2020)
smartphone.display()

