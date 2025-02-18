class Employee:
    count = 0

    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience

        Employee.count += 1

    
    
    def designation(self):
        if self.experience <= 0:
            return "Fresher"
        
        elif self.experience <= 2:
            return "Junior Software Engineer"
    
        elif self.experience > 2 and self.experience <= 5:
            return "Mid Senior Software Engineer"
        
        else:
            return "Senior Software Engineer"


    @property
    def increment_salary(self, increment_amount):
        self.salary = self.salary + increment_amount

    
    
    # object method
    def bonus(self):
        # (0-2) : 7% (2-5) : 15% (5-10) : 20% () : 25%
        
        if self.experience < 0:
            return 0
        
        if self.experience >=0 or self.experience <= 2:
            amount = self.get_percentage(total=self.salary, percent=7)
        elif self.experience > 2 or self.experience <= 5:
            amount = self.get_percentage(total=self.salary, percent=15)
        elif self.experience > 5 or self.experience <= 10:
            amount = self.get_percentage(total=self.salary, percent=20)
        else:
            amount = self.get_percentage(total=self.salary, percent=25)
        
        
        return amount


    # class method
    @classmethod
    def total_employee(cls):
        return cls.count
    
    @staticmethod # just adding functionality
    def get_percentage(total, percent):
        return (total * percent) / 100

        

e1 = Employee(name="Nahid", salary=20000, experience=5)
e2 = Employee(name="Salman", salary=50000, experience=8)

print(Employee.total_employee())

# print(e1.designation)
# e1.increment_salary(increment_amount=1000)
# e2.increment_salary(increment_amount=1500)

# print(e1.bonus())
# print(e2.bonus())

# study about class, object method, property getter setter