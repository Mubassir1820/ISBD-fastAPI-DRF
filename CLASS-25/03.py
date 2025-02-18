# access modifier

from datetime import datetime

class User:
    def __init__(self, email):
        self.email = email

        # Private attribute
        self.__joined_at = datetime.now()

    # Protected
    def _joined(self):
        return self.__joined_at.strftime("%d-%m-%Y")
    
# global space
u1 = User(email="demo@abc.com")

# Forbidden in OOP philosophy(user of protected)
print(u1._joined())

# (Use of private) -> BOOM -> got error
# print(u1.__joined_at)



# print(u1._User__joined_at)