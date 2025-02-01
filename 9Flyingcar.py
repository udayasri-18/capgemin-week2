class Car:
    def __init__(self):
        pass
    def move(self):
        print("Car moves on the road")
class Airplane:
    def __init__(self):
        pass
    def move(self):
        print("Airplane flies in the sky")
class FlyingCar(Car,Airplane):
    def __init__(self):
        super().__init__()
    def move(self):
        print("Flyingcar moves on road also flies in the sky")

flyingcar=FlyingCar()
flyingcar.move()

# a=Airplane()
# a.move()

# c=Car()
# c.move()