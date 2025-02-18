ls = [
    ('Alice', 25),
    ('Marley', 30),
    ('Bob', 5),
]

# Sort Based on 'age'
ls = sorted(ls , key = lambda ls : ls[1] , reverse=False)

print(ls)