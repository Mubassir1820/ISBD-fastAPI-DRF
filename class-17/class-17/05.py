dc1 = {
    "name" : "salman",
    "age" : 10
}

# Dictionary unpack
dc2 = {**dc1}

dc2['name'] = "nahid"


print(dc1)
print(dc2)