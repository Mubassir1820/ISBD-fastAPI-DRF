# If an object has no attribute then set a default value for that attribute

class Pet:
    def __init__(self, price):
        self.price = price

p1 = Pet(10000)

# print(p1.location) #error

# loc = getattr(p1, "location", "Dhaka")
# print(loc)

loc = getattr(p1, "location", False)
if loc is False:
    setattr(p1, "location", "Dhaka")

print(p1.location)

# Get attribute sets the value of that dynamic attribute temporaily where setattr permanent
# Implement __hash__. What it is and how to use it