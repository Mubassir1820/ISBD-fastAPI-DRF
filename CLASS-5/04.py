# List of dictionaries

"""
[
    {},
    {},
    {},
]


"""

persons = [
    {'name': 'abc', 'age': 25}, # index-0
    {'name': 'def', 'age': 15}, # index-1
    {'name': 'Xyz', 'age': 30}, # index-2
]

first_person = persons[0]
print(first_person)

print(first_person.get('name'))

# Do it once
person_name = persons[0].get('name')
print(person_name)