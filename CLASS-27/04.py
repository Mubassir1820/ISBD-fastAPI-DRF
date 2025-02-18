from typing import Dict

"""
try:
    # try to execute some code
except:
    print("Some Error")
finally:

"""



def process_entity(person: Dict):
    if person["salary"] < 5000:
        raise ValueError("Salary too low")
    cal = person['salary'] / person['tax']
    return cal

p = {
    "salary": 1000,
    "tax": 0
}

print("Before")

try:
    # dangerous code
    process_entity(person=p)
except ZeroDivisionError as e:
    print("ZeroDivisionError: ", e)
except KeyError as e:
    print("Key not found: ", e)
except ValueError as e:
    print("Key not found: ", e)
except Exception as e:
    print(e)
finally:
    print("Finally Block")


print("After")



# self study: How to create custom error class in python