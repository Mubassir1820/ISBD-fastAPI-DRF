ls = [("Alice", 25), ("Sakib", 10), ("rakib", 35)]

# print(sorted(ls))

#  sort based on age (age -> sort key)
ls = [("Sakib", 10), ("Alice", 25), ("rakib", 35)]

SORT_KEY = 1

for item in ls:
    # print(item[1])
    print(item[SORT_KEY])
