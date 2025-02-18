class Employee:
    # Class Attribute
    count = 0

    # Constructor(Will be called automatically when object initialization)
    def __init__(self, name: str):
        self.name = name
        Employee.count = Employee.count + 1
        
e1 = Employee(name='a')
print(e1.count)
e2 = Employee(name='b')
print(e2.count)
e3 = Employee(name='c')
print(e3.count)
e4 = Employee(name='d')
print(e4.count)

print(e1.count, e2.count, e3.count, e4.count)