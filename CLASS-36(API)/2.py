import requests

endpoint = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(endpoint)

# print(response.json())
# print(response.status_code)

all_post = response.json()

for post in all_post:
    if post.get('id') == 10:
        print(post)