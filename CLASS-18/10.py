person = {  'name': 'Salman',
            'Age': 10,
            'email': 'Example.com',
            'bio': 'CEO of Innovative Skills',
            'expertise': 'ML/DL/AI'}

# If the key doesnt exist in the dict
w = person.setdefault('university', 'NSU')

print(w)

print(person)