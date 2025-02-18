# class Person():
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def Display(self):
#         print(self.name, self.id)

# class Emp(Person):

#     def print(self):
#         print("Emp child class was called")

# # emp = Person(name="Mubassir", id=1812927042)
# emp = Emp(name="Mubassir", id=1812927042)
# # emp.Display()

# # emp.Display()
# # emp.print()
# print(emp.name)






# super().__init__

# class A():
#     def __init__(self, name = "Mubassir"):
#         self.name = name

# class B(A):
#     def __init__(self, roll):
#         self.roll = roll

# obj1 = B(23)
# obj1.name


# from datetime import datetime

# class User:
#     def __init__(self,email):
#         self.email = email
#         self.joined_at = datetime.now()

#     def joined(self):
#         return self.joined_at.strftime("%d-%m-%Y")
    
# # child class
# class Userbio(User):
#     def __init__(self, email, profile_img, bio):
#         super().__init__(email=email)
#         self.profile_img = profile_img
#         self.bio = bio

# class Employee(User):
#     def __init__(self, email, salary):
#         super().__init__(email)
#         self.salary = salary



from datetime import datetime

class User:
    def __init__(self, email):
        self.email = email

        # Private attribute
        self.__joined_at = datetime.now()

    # Protected
    def _joined(self):
        return self.__joined_at.strftime("%d-%m-%Y")
    
class UserBio(User):
    def __init__(self, email, profile_image, bio):
        # Super constructor
        super().__init__(email=email)
        self.profile_image = profile_image

    def intro(self):
        # Dont use the private attribute evenif there are no errors
        print(self.__joined_at)
        return f"He is the member of ISBD and joined at {self._joined()}"
    
obj1 = UserBio(email="mh.ipsc",profile_image="",bio="Hello")
obj1.intro()