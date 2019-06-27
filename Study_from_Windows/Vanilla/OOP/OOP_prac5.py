class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def study(self):
        print(self.name + ' studies hard.')

class Employee(Person):

    def work(self):
        print(self.name + ' works hard')

stu = Student("Dave")
emp = Employee("John")

print(stu.study())
print(emp.work())
