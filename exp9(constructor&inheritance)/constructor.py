1.Write a program for default constructor and parametrized constructor . Use class student with data menbers -rno , name, address . 
class Student:
    def __init__(self, rno=0, name="Unknown", address="Unknown"):
        self.rno = rno
        self.name = name
        self.address = address

    def display(self):
        print(f"Roll No: {self.rno}, Name: {self.name}, Address: {self.address}")

print("Default Constructor")
s1 = Student()
s1.display()

print("\nParameterized Constructor")
s2 = Student(101, "ABC", "Pune")
s2.display()



2. Create a class Employee with data members: name, department and salary. Create
suitable methods for reading and printing employee information
class Employee:
    def read_info(self):
        self.name = input("Enter Employee Name: ")
        self.department = input("Enter Department: ")
        self.salary = input("Enter Salary: ")

    def print_info(self):
        print("\nEmployee Details")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

emp = Employee()
emp.read_info()
emp.print_info()
