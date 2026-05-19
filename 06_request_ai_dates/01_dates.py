# Hacer peticiones a una API en python
# con y sin dependencias

# 1. Sin dependencias (dificil y sin dependencias)
import requests
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts"

# try:
# response = urllib.request.urlopen(api_posts)
#  data = response.read()
#   json_data = json.loads(data.decode("utf-8"))
# print(json_data)
#    response.close()
# except urllib.error.URLError as error:
# print(f"Error: {error}")

# 2. Con dependencias (facil y con dependencias)
print("\nGET con requests")

api_posts = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(api_posts)
# print(response.json())


# 3. POST
print("\nPOST con requests")
input = {
    "title": "foo",
    "body": "bar",
    "userId": 12,
}

response = requests.post(api_posts, json=input)
# print(response.json())


# 4. PUT
print("\nPUT con requests")
try:
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts",
        json={
            "id": 1,
            "title": "foo",
            "body": "bar",
            "userId": 1,
        },
    )
    print(response.status_code)
except requests.exceptions.RequestException as error:
    print(f"Error: {error}")
print(response.json())
