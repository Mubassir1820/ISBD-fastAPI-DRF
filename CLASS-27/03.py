from typing import Dict

"""
try:
    # try to execute some code
except:
    print("Some Error")

"""



def process_entity(person: Dict):
    cal = person['salary'] / person['tax']
    return cal

p = {
    "salary": 1000,
    "tax": 10
}

print("Before")

try:
    # dangerous code
    process_entity(person=p)
except Exception as err:
    print(err)

print("After")