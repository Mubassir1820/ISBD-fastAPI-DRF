import requests

endpoint = "https://jsonplaceholder.typicode.com/posts/18"

response = requests.get(endpoint)

# print(response.json())
# print(response.status_code)

post = response.json()


print(post)