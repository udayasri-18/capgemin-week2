class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        if quantity<=self.stock:
            return "Requested quantity is available"
        else:
            return "Not available"
p=Product('bat',200,20)
print(p.check_availability(21))
print(p.check_availability(2))