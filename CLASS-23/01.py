from datetime import datetime

# Blueprint
class Employee:
    
    # Constructor(Will be called automatically when object initialization)
    def __init__(self, name: str, salary: int, age: int, **kwargs):
        self.name = name
        self.salary = salary
        self.age = age
        self.dummy_attribute = kwargs.get('dummy_attribute')
        

    # Method
    def get_year_of_born(self):
        #curent_year - self.age = ? year
        current_year = datetime.now().year
        year_of_born = current_year - self.age
        return year_of_born
        # Dont introduce any new attribues in method
        # Only reassign value to the existing attributr/ simple returning a value

e1 = Employee(name="Mubassir", salary=50000, age=25)
e2 = Employee(name="Musarat", salary=400, age=21)
print(e1.get_year_of_born()) 
print(e2.get_year_of_born()) 