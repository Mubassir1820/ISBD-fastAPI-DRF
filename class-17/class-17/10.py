person = {
    'name': 'salman', 
    'age': 10,
    'email': 'yahoo.com', 
    'bio': 'CEO of innovative Skills',
    'expertise': 'ML / DL / AI'
}

# if any key not exists in the dictionary
w = person.setdefault('university' , 'UAP')


person['email'] = "example.com"
# person['city'] = 'Dhaka' # not recommended

print(w)

print(person)


if 'email' in person:
    person['email'] = 'yahoo.com'
else:
    person.setdefault('email', 'Dhaka')