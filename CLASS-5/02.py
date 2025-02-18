student1 = {
    "name": "Abc",
    "roll": 5,
    "class": 10,
    "school": "High School",
}

# Approach-1 (bracket notation)
# dictionary name[key_name]

print(student1['name'])
print(student1['roll'])
print(student1['class'])
print(student1['school'])

# Approach-2 (using .get() method)
# dictionary_name.get("key_name")

print(student1.get("name"))
print(student1.get("roll"))