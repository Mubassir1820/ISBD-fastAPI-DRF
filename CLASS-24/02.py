# Operator overloading

class Employee:

    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience


    def __eq__(self, other):
        return self.experience == other.experience    

    def __add__(self, amount):
        self.salary = self.salary + amount 

e1 = Employee(name="Nahid", salary=20000, experience=5)
e3 = Employee(name="Salman", salary=50000, experience=8)

# print(e1 == e3)


e1 + 1500

print(e1.salary)