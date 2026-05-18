# Hacer peticiones a una API en python
# con y sin dependencias

# 1. Sin dependencias
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts"

response = urllib.request.urlopen(api_posts)
data = response.read()
json_data = json.loads(data.decode("utf-8"))
print(json_data)
response.close()
