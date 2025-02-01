class Employee:
    # def __init__(self,name,id,dept):
    #     self.name=name
    #     self.id=id
    #     self.dept=dept
    name=input("Enter employee name: ")
    id=int(input("Enter employee id: "))
    department=input("Enter employee department: ")
    def printInfo(self):
        print(f"Employee name :{self.name} id:{self.id} department: {self.department}")

# name=input("Enter employee name: ")
# id=int(input("Enter employee id: "))
# department=input("Enter employee department: ")

emp=Employee()
emp.printInfo()