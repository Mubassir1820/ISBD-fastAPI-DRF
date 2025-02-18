def get_sort_key_value(ls, key):

    for item in ls:
        print(item[key])


ls = [("Sakib", 10), ("Alice", 25), ("rakib", 35)]

# get_sort_key_value(ls=ls, key=1)

new_ls = [
    ("Computer", 40000, "India"),
    ("Mobile", 10000, "China"),
    ("Dress", 500, "Bangladesh"),
]


get_sort_key_value(ls=new_ls, key=1)
