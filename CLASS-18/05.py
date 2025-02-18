dc1 = {
    "name": "Salman",
    "Age": 10
}

# dictionary unpack
dc2 = {**dc1}

dc2["name"] = "Nahid"

print(dc2)
print(dc1)