# Inheritence

from datetime import datetime
# Parent class/Base class/Super class
class User:
    def __init__(self, email):
        self.email = email
        self.joined_at = datetime.now()

    def joined(self):
        return self.joined_at.strftime("%d-%m-%Y")

# Chile class/derived class
class UserBio(User):
    def __init__(self, email, profile_image, bio):
        # super constructor
        super().__init__(email=email)
        self.profile_imgage = profile_image
        self.bio = bio

class Employee(User):
    def __init__(self,email,salary):
        super().__init__(email)
        self.salary = salary

u1 = UserBio(email="Demo@gmail.com", profile_image="demo.jpg", bio="Simple!")

print(u1.email)
print(u1.joined())   

e1 = Employee(email="abc@gmail.com", salary=20000)


# Inheritence hell