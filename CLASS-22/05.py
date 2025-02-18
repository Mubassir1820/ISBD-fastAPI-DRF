# Attributes
# First name, last name, email

from datetime import datetime
import pprint

class Person: 
    # constructor/python calls it as initializer
    def __init__(self, first_name , last_name, email, message):
        # print("Hello")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.joined = datetime.now()


    # dunder (double ubderscore)
    def __str__(self):
        return f"He is {self.first_name}"

nahid_obj = Person(first_name="md", last_name="Nahid", email="abc@gmail.com", message="Whatup")
# slaman = Person()
# salman_obj = Person(first_name="Salman", last_name="Sultan",email="def@example.com", message='LOL')
# print(nahid_obj.first_name)
# print(nahid_obj.joined)
# print(nahid_obj)
# print(dir(salman_obj.__dict__))
# pprint(dir(salman_obj.__dict__))

print(nahid_obj)

# Why do we use self
# Self study about pprint