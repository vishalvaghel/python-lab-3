class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_person_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Job:
    def _init_(self, designation, salary):
        self.designation = designation
        self.salary = salary

    def display_job_details(self):
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")

class Employee(Person, Job):
    def __init__(self, name, age, designation, salary):
        Person._init_(self, name, age)
        Job._init_(self, designation, salary)

    def display_employee_details(self):
        self.display_person_details()
        self.display_job_details()

Employee1 = Employee("Bob Smith", 30, "Project Manager", 120000)

Employee1.display_employee_details()