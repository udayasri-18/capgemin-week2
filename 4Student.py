class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def studentdetails(self):
        print(f"Student name:{self.name} rollno:{self.rollno}")

name=input("Enter name of student:")
rollno=int(input("Enter rollno: "))
student=Student(name,rollno)
student.studentdetails()