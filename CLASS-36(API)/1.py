import json

# user data dictionary
user_data = {"id": 1, "name": "Mubassir"}

print(user_data)
print(type(user_data))


# convert dict to json
user_json = json.dumps(user_data)


print(user_json)
print(type(user_json)) #str as no types named json in python


# convert JSON to dict
user_data_new = json.loads(user_json)


print(user_data_new)