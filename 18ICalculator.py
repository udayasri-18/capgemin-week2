from abc import ABC,abstractmethod
class IDCalculator(ABC):
    
    def add(self):
        pass
    
    def subtract(self):
        pass
    
    def multiply(self):
        pass
    
    def divide(self):
        pass
class Basiccalculator(IDCalculator):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        sum=self.a+self.b
        print(f"Sum is {sum}")
    def subtract(self):
        diff=abs(self.a-self.b)
        print(f"Difference is {diff}")
    def multiply(self):
        mul=self.a*self.b
        print(f"Multiplication is {mul}")
    def divide(self):
        div=self.a/self.b
        print(f"Division is {div}")
    

calculator=Basiccalculator(5,9)
calculator.multiply()
calculator.divide()
calculator.add()
calculator.subtract()