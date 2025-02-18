def get_value(any_list, key):
    for item in any_list:
        print(item[key])

ls = [
    ('Alice', 25),
    ('Bob', 5),
    ('Marley', 30),
]


get_value(any_list=ls,key=1)