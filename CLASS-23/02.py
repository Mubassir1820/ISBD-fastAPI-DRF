class Employee:
    # Class Attribute
    count = 0

    # Constructor(Will be called automatically when object initialization)
    def __init__(self, name: str):
        self.name = name
        print("-------")
        print(self.count) 
        self.count = self.count + 1
        print(self.count)
        print("--------")
        
e1 = Employee(name='a')
e2 = Employee(name='b')
e3 = Employee(name='c')
e4 = Employee(name='d')

print(e1.count, e2.count, e3.count, e4.count)
# Not incrementing as count is a class attribute, and has to be called by Employee.count