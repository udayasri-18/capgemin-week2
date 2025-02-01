class Shape:
    def __init__(self):
        pass
    def area(self):
        print("Area is: ")
class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length=length
    def area(self):
        area=self.length**2
        print("Area of square is",area)
class Triangle(Shape):
    def __init__(self,length,breadth):
        super().__init__()
        self.length=length
        self.breadth=breadth
    def area(self):
        area=self.length*self.breadth*0.5
        print("Area of Triangle is",area)
triangle=Triangle(2,9)
triangle.area()

square=Square(4)
square.area()