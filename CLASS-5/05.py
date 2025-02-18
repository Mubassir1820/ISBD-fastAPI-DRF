# Dictionary with lists

author = {
    'name': 'Humayun Ahmde',
    'books': ['one','two'],
    'children': [
        {'name': 'Nuhas', 'age': 30},
        {'name': 'Ninit', 'age': 10},
    ]
}


age = author.get("children")[0].get("age")
print(f'age is {age}')

second_book = author.get('books')[1]
print(second_book)

# SELF STUDY: tuple, set, tuple vs list, how to access tuple elements