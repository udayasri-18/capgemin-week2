from abc import ABC,abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(IVehicle):
    def start_engine(self):
        print(f"Car engine start")
    def stop_engine(self):
        print(f"Car engine stop")
class Bike(IVehicle):
    def start_engine(self):
        print(f"Bike engine start")
    def stop_engine(self):
        print(f"Bike engine stop")
class Truck(IVehicle):
    def start_engine(self):
        print(f"Truck engine start")
    def stop_engine(self):
        print(f"Truck engine stop")
truck=Truck()
truck.start_engine()
truck.stop_engine()
print()
car=Car()
car.start_engine()
car.stop_engine()
print()
bike=Bike()
bike.start_engine()
bike.stop_engine()