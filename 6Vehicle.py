class Vehicle:
    def __init__(self):
        print("Vehicle class constructor")
    def showv(self):
        print("Vehicle method")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("Car class constructor")
    def showc(self):
        print("car method")
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        print("Bike class constructor")
    def showb(self):
        print("bike method")
class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        print("Electric car constructor")
    def showe(self):
        print("Electric car method")
vehicle=Vehicle()
vehicle.showv()
print()
car=Car()
car.showv()
car.showc()
print()
bike=Bike()
bike.showv()
bike.showb()
print()
electriccar=ElectricCar()
electriccar.showv()
electriccar.showc()
electriccar.showe()
