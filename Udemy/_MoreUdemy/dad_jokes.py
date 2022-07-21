import requests
from random import choice

user_input = input("What do you want to search for?")
url = "https://icanhazdadjoke.com/search"

response = requests.get(url, headers={"Accept": "application/json"}, params={"term": user_input})
json_data = response.json()
num_jokes = json_data["total_jokes"]


if num_jokes == 0:
    print(f"There are no jokes about {user_input}")
elif num_jokes == 1:
    print(json_data["results"]["joke"])
else:
    random_joke = choice(json_data["results"])["joke"]
    print(f"There are {num_jokes} jokes about {user_input}. Here is one:")
    print(random_joke)


