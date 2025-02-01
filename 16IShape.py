from abc import ABC,abstractmethod
class IShape(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def calculate_area(self):
        print("Area is: ")
class Circle(IShape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
    def calculate_area(self):
        area=3.14*(self.radius**2)
        print("Area of circle is",area)
class Rectangle(IShape):
    def __init__(self,length,breadth):
        super().__init__()
        self.length=length
        self.breadth=breadth
    def calculate_area(self):
        area=self.length*self.breadth
        print("Area of Rectangle is",area)
rectangle=Rectangle(2,9)
rectangle.calculate_area()
Circle(4).calculate_area()