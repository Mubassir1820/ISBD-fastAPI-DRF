# Polymorphism -> Method overloading

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

class SalesMan(Employee):
    def __init__(self, salary, incentive):
        super().__init__(salary)
        self.incentive = incentive

    # Redefine (Method Overloading)
    def get_salary(self):
        return self.salary + self.incentive

e1 = Employee(salary=10000)
s1 = SalesMan(salary=8000, incentive=500)

print(e1.get_salary())
print(s1.get_salary())