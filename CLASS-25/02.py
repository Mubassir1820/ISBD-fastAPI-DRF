# encapsulation -> access modifier
#  4 pillars of python

"""
Access Modifier:
1. Public attribute / Public Method
2. Protected attribute / Protected method
3. Private attribute / Private Method
"""

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
    