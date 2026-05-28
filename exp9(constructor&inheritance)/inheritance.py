1. Python program to read and print students information using two classes using
simple inheritance.
class Person:
    def read_person(self):
        self.name = input("Enter student name: ")

    def print_person(self):
        print(f"Name: {self.name}")

class Student(Person):
    def read_student(self):
        self.read_person()
        self.roll_no = input("Enter roll number: ")

    def print_student(self):
        print("\nStudent Info")
        self.print_person()
        print(f"Roll No: {self.roll_no}")

s = Student()
s.read_student()
s.print_student()


2. Write a Python program to implement multiple inheritance
class Parent1:
    def m1(self):
        print("Parent1 class")
class Parent2:
    def m2(self):
        print("Parent2 class")
class child(Parent1, Parent2):
    def m3(self):
        print("Child class")

child = child()
child.m1()
child.m2()
child.m3()
