class Person:
    def __init__(self,name):
        self.name=name
    def displayperson(self):
        print(f"Person name: {self.name}")
class Employee(Person):
    def __init__(self, name,id):
        super().__init__(name)
        self.id=id
    def displayemployee(self):
        print(f"Employee name:{self.name} id:{self.id}")
class Manager(Employee):
    def __init__(self, name,id,dept):
        super().__init__(name, id)
        self.dept=dept
    def displaymanager(self):
        print(f"Manager name:{self.name} id:{self.id} department:{self.dept}")
    def approve_leave(self,days):
        if days<26:
            print("Leave is not approved")
        else:
            print(f"Leave approved for {self.name} id:{self.id}")

manager=Manager('udayasri',22,'cse')
manager.displaymanager()
manager.displayemployee()
manager.displayperson()
print()
employee=Employee('udaya',9)
employee.displayemployee()
employee.displayperson()
print()
person=Person('Sri')
person.displayperson()
print()
manager.approve_leave(22)
manager.approve_leave(29)
